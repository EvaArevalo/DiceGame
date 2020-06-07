import random
import numpy as np

GOAL = 12
action_A = {'reward':6, 'prob':1/6, 'match':[6]}
action_B = {'reward':3, 'prob':1/3, 'match':[2,3]}
action_C = {'reward':2, 'prob':1/2, 'match':[4,5,6]}
actions = [action_A,action_B,action_C]

def ss2p_a(**kwargs):
	return action_A

def ss2p_b(**kwargs):
	return action_B

def ss2p_c(**kwargs):
	return action_C

def ss2p_r(**kwargs):
	ix = random.randint(0,2)
	return actions[ix]

def ss2p_4(**kwargs):
	'''if diff<=4,A, if diff>=6, B, if diff>=9, C'''
	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	#get diff
	diff = profit_opp-profit_own
	if diff <=4:
		return action_B
	elif diff >= 6:
		return action_A
	elif diff >= 9:
		return action_C

def ss2p_5(**kwargs):
	'''If I get pt and 2nd didn’t get pt then I go down. 
	If I didn't get pt and 2nd get pt then I go up. If neither, remain. '''
	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		prev_action_own = kwargs['prev_action_p1']
		prev_action_opp = kwargs['prev_action_p2']

	else:
		prev_action_own = kwargs['prev_action_p2']
		prev_action_opp = kwargs['prev_action_p1']
	prev_ix_own = actions.index(prev_action_own)
	prev_ix_opp = actions.index(prev_action_opp)
	prev_dice_res = kwargs['prev_dice_res']

	#find out who won
	if prev_dice_res in prev_action_own['match']: 
		own_win = True
	else:
		own_win = False

	if prev_dice_res in prev_action_opp['match']: 
		opp_win = True
	else:
		opp_win = False

	#logic
	if own_win and not opp_win:
		if prev_dice_res in prev_action_own['match']: ##success
			new_ix = max(prev_ix_own-1,0) ##go down
		else:
			new_ix = min(prev_ix_own+1,2) ##go up

	elif not own_win and opp_win:
		if prev_dice_res in prev_action_own['match']: ##success
			new_ix = min(prev_ix_own+1,2) ##go up
		else:
			new_ix = max(prev_ix_own-1,0) ##go down

	else:
		new_ix = prev_ix_own

	return actions[new_ix]

def ss2p_6(**kwargs):
	'''+3 以上 A
	±2 之間 C
	±3 之間 B
	−3 以下 A'''
	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
	throws = kwargs['throws']

	#get diff
	diff = profit_own-profit_opp
	if diff < -3:
		return action_A
	elif diff >= -2 and diff <=2  :
		return action_C
	elif diff>=-3 and diff <=3 :
		return action_B
	elif diff > 3:
		return action_A

def ss2p_7(**kwargs):
	'''always follow player p1'''
	return kwargs['sel_action_p1']

def ss2p_8(**kwargs):
	'''use strategy a when the point less than the opponent,use strategy b 
	when the points of two players are equal,then use strategy c when the \
	point more than the opponent'''
	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	#get diff
	if profit_own < profit_opp:
		return action_A
	elif profit_own == profit_opp:
		return action_B
	elif profit_own > profit_opp:
		return action_C

def ss2p_9(**kwargs):
	'''Play A until he gets a reward, the nwitches to B'''
	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	#return action according to profit
	if profit_own < 6:
		return action_A
	elif profit_own >6:
		return action_B


'''args_p2 = {'profit_p1':profit_p1,'profit_p2':profit_p2,\
			  'throws':throws, 'prev_action_p1':prev_action_p1,\
			  'prev_action_p2':prev_action_p2,\
			  'prev_dice_res':prev_dice_res,\
			  'sel_action_p1':sel_action_p1}'''
