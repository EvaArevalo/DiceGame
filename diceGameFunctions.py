import random
import numpy as np

GOAL = 12
action_A = {'reward':6, 'prob':1/6, 'match':[6]}
action_B = {'reward':3, 'prob':1/3, 'match':[2,3]}
action_C = {'reward':2, 'prob':1/2, 'match':[4,5,6]}
actions = [action_A,action_B,action_C]

def play_dice_game_1p(selection_strategy, initialization_strategy, rounds=100):
	'''play dice game, 1 player. 
	INPUT: selection_strategy,initialization_strategy, rounds
	OUTPUT: average No. of throws over rounds rounds
	'''
	dice_throws_arr = []

	for i in range(0,rounds):
		
		#vars
		profit = 0
		throws = 0
		win = 0
		prev_action = initialization_strategy() #choose a random action to begin
		prev_dice_res = random.randint(1,6)

		while profit < GOAL:
			
			#sel action, roll dice, count reward
			kwargs = {'profit':profit,'throws':throws, 'prev_action':prev_action,\
					 'prev_dice_res':prev_dice_res, 'win':win}
			sel_action = selection_strategy(**kwargs)
			dice_res = random.randint(1,6)
			if dice_res in sel_action['match']:
				win += 1
				profit += sel_action['reward']
			
			#update state
			throws += 1
			prev_action = sel_action
			prev_dice_res = dice_res

		dice_throws_arr.append(throws)
	
	avg = np.mean(dice_throws_arr)
	print('Player averaged '+ str(avg) + ' throws for '+ str(rounds) +' rounds')

def play_dice_game_2p(selection_strategy_p1,selection_strategy_p2,\
	initialization_strategy_p1, initialization_strategy_p2,\
	rounds=100):
	'''play dice game, 2 players. 
	INPUT: selection_strategy,initialization_strategy, rounds
	OUTPUT: winner array containing 1 for p1 win, 2 for p2 win and 0 for draw
	'''
	winner_array = []

	for i in range(0,rounds):
		profit_p1 = 0
		profit_p2 = 0
		win_p1 = 0
		win_p2 = 0
		throws = 0
		prev_action_p1 = initialization_strategy_p1()  #choose a random action to begin
		prev_action_p2 = initialization_strategy_p2() #choose a random action to begin
		prev_dice_res = -1

		while profit_p1 < GOAL and profit_p2 < GOAL:
			#select strategy
			args_p1 = {'profit_p1':profit_p1,'profit_p2':profit_p2,\
					  'throws':throws, 'prev_action_p1':prev_action_p1,\
					  'prev_action_p2':prev_action_p2,\
					  'prev_dice_res':prev_dice_res, \
					  'win_p1':win_p1,'win_p2':win_p2,'whoAmI':'p1'}
			sel_action_p1 = selection_strategy_p1(**args_p1)
			args_p2 = {'profit_p1':profit_p1,'profit_p2':profit_p2,\
					  'throws':throws, 'prev_action_p1':prev_action_p1,\
					  'prev_action_p2':prev_action_p2,\
					  'prev_dice_res':prev_dice_res, \
					  'win_p1':win_p1,'win_p2':win_p2,'whoAmI':'p2',\
					  'sel_action_p1':sel_action_p1}
			sel_action_p2 = selection_strategy_p2(**args_p2)
			
			#check reward
			dice_res = random.randint(1,6)
			if dice_res in sel_action_p1['match']:
				profit_p1 += sel_action_p1['reward']
			if dice_res in sel_action_p2['match']:
				profit_p2 += sel_action_p2['reward']

			#update
			throws += 1
			prev_action_1 = sel_action_p1
			prev_action_2 = sel_action_p2
			prev_dice_res = dice_res
		
		if profit_p1==profit_p2:
			win_p1 += 1
			win_p2 += 1
			winner_array.append(0)
		elif profit_p1>profit_p2:
			win_p1 += 1
			winner_array.append(1)
		elif profit_p1<profit_p2:
			win_p2 += 1
			winner_array.append(2)
			
	#decide winner
	winner_array = np.array(winner_array)
	chooseWinner(winner_array,rounds)

def chooseWinner(winner_arr,rounds):
	
	p2 = len(np.where(winner_arr==2)[0])
	p1 = len(np.where(winner_arr==1)[0])
	draws = rounds - p1 - p2
	
	if p1==p2:
		print('Draw between player 1 and 2')

	elif p1>p2:
		print('Player 1 wins ' + str(p1) + ' vs. ' + str(p2) +' and ' + str(draws) + ' draws.')

	elif p2>p1:
		print('Player 2 wins ' + str(p2) + ' vs. ' + str(p1) +' and ' + str(draws) + ' draws.')
