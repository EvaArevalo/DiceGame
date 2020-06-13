import random
import numpy as np

GOAL = 12
action_A = {'reward':6, 'prob':1/6, 'match':[6]}
action_B = {'reward':3, 'prob':1/3, 'match':[2,3]}
action_C = {'reward':2, 'prob':1/2, 'match':[4,5,6]}
actions = [action_A,action_B,action_C]

def ss1p_a(**kwargs):
	return action_A

def ss1p_b(**kwargs):
	return action_B

def ss1p_c(**kwargs):
	return action_C

def ss1p_r(**kwargs):
	ix = random.randint(0,2)
	return actions[ix]

def ss1p_1(**kwargs):
	''' Reinforcement learning based ....'''
	profit = kwargs['profit']

	if profit==0:
		return action_B
	elif profit==2:
		return action_C
	elif profit==3:
		return action_B
	elif profit==4:
		return action_C
	elif profit==5:
		return action_C
	elif profit==6:
		return action_A
	elif profit==7:
		return action_C
	elif profit==8:
		return action_C
	elif profit==9:
		return action_B
	elif profit==10:
		return action_C
	
def ss1p_5(**kwargs):
	throws = kwargs['throws']
	if throws%2 == 0:
		return action_A
	else:
		return action_B
	
def ss1p_6(**kwargs):
	throws = kwargs['throws']
	if throws%2 == 0:
		return action_A
	else:
		return action_C

def ss1p_7(**kwargs):
	throws = kwargs['throws']
	if throws%2 == 0:
		return action_B
	else:
		return action_C
	
def ss1p_8(**kwargs):
	threshold = 0.4
	rand = random.randint(1,10)
	if rand > threshold:
		return action_B
	else:
		return action_C
	
def ss1p_9(**kwargs):
	if kwargs['prev_action']==action_A:
		return action_B
	elif kwargs['prev_action']==action_B:
		return action_C
	elif kwargs['prev_action']==action_C:
		return action_A

def ss1p_10(**kwargs):
	''' Up the stakes if success in previous round, down the stakes otherwise'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	prev_ix = actions.index(prev_action)
	
	if prev_dice_res in prev_action['match']: ##success
		new_ix = min(prev_ix+1,2)
		return actions[new_ix]
	else:
		new_ix = max(prev_ix-1,0) 
		return actions[new_ix]

def ss1p_11(**kwargs):
	''' use strategy b to reach 6 points,then use strategy c.'''
	profit = kwargs['profit']

	if profit < 6:
		return action_B
	else:
		return action_C

def ss1p_12(**kwargs):
	''' Down the stakes if success in previous round, up the stakes otherwise'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	prev_ix = actions.index(prev_action)
	
	if throws==0:
		return action_C
	elif prev_dice_res in prev_action['match']: ##success
		new_ix = max(prev_ix-1,0)
		return actions[new_ix]
	else:
		new_ix = min(prev_ix+1,2)
		return actions[new_ix]

def ss1p_13(**kwargs):
	''' use strategy b to reach 6 points,then use strategy a.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	
	if profit<6:
		return action_B
	else:
		return action_A
   
def ss1p_14(**kwargs):
	''' use strategy b , use a sometimes if win a lot.'''
	win = kwargs['win']
	throws = kwargs['throws']
	
	if win/throws>0.8:
		return action_A
	else:
		return action_A

def ss1p_15(**kwargs):
	'''Play A until he gets a reward, the nwitches to B'''
	#get kwargs
	profit = kwargs['profit']

	#return action according to profit
	if profit < 6:
		return action_A
	else:
		return action_B

def ss1p_16(**kwargs):
	'''Play B 2 in a row, then A 2 in a row'''
	#get kwargs
	throws = kwargs['throws']

	#return action according to profit
	if throws == 0:
		return action_B
	elif count_B < 2:
		count_A = 0
		count_B += 1
		return action_B
	elif count_B >= 2:
		count_B = 0
		count_A += 1
		return action_A

def ss1p_17(**kwargs):
	''' use strategy A to reach 6 points,then use strategy C.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	
	if profit<6:
		return action_A
	else:
		return action_C

def ss1p_18(**kwargs):
	''' use strategy C to reach 6 points,then use strategy A.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	
	if profit<6:
		return action_C
	else:
		return action_A

def ss1p_18(**kwargs):
	''' use strategy C to reach 6 points,then use strategy A.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	
	if profit<6:
		return action_C
	else:
		return action_A

def ss1p_19(**kwargs):
	''' use strategy A if throws==0,throws==1, then use strategy B.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']
	
	if throws==0 or throws==1:
		return action_A
	else:
		return action_B

def ss1p_20(**kwargs):
	''' use strategy B to reach twice,then use strategy C.'''
		#get kwargs
	throws = kwargs['throws']

	if throws==0 or throws==1:
		return action_B
	else:
		return action_C
	
def ss1p_21(**kwargs):
	''' use strategy B twice, A twice, C 3 times'''
		#get kwargs
	throws = kwargs['throws']
	
	if throws==0 or throws==1:
		return action_B
	elif throws==2 or throws==3:
		return action_A
	else:
		return action_C	

def ss1p_22(**kwargs):
	''' 玩家採取先由較容易取分的C方案來累積分數，
	之後選擇挑戰A方案，成功後只選擇C方案'''
		#get kwargs
	throws = kwargs['throws']
	profit = kwargs['profit']

	if profit<2:
		return action_C

	elif profit<8:
		return action_A

	else:
		return action_C

def ss1p_23(**kwargs):
	''' B until profit=2, A until profit=8, then B'''
		#get kwargs
	throws = kwargs['throws']
	profit = kwargs['profit']

	if profit<3:
		return action_B

	elif profit<9:
		return action_A

	else:
		return action_B

def ss1p_24(**kwargs):
	''' C until profit=2, B until profit=8, then C
	return action_a if turns>=9'''
		#get kwargs
	throws = kwargs['throws']
	profit = kwargs['profit']

	if throws>=9:
		return action_A

	if profit<2:
		return action_C

	elif profit<8:
		return action_B

	else:
		return action_C

def ss1p_25(**kwargs):
	'''action_B until 4 times or 6p, action_C otherwise'''
	#get kwargs
	throws = kwargs['throws']
	profit = kwargs['profit']

	if profit>6 or throws>=4:
		return action_C
	else:
		return action_B

def ss1p_26(**kwargs):
	'''action_B 4 times, C 3 times, B until win'''
	#get kwargs
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_dice_res = kwargs['prev_dice_res']
	prev_action = kwargs['prev_action']


	if prev_dice_res not in prev_action['match']:
		fail+=1
	else:
		fail=0

	if prev_action==action_B and fail<2:
		counter_C=0
		return action_B
	elif counter_C<2:
		counter_C += 1
		return action_C
	else:
		counter_C=0
		return action_B

def ss1p_27(**kwargs):
	'''If profit_own<6 action_A, else action_B.'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	
	if profit<6:
		return action_A
	else:
		return action_B

def ss1p_28(**kwargs):
	'''Start with A, lower the stakes on fail'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']

	if throws==0:
		return action_A

	elif prev_action==action_A:
		if prev_dice_res in prev_action['match']: 
			return action_A
		else:
			return action_B

	elif prev_action==action_B and prev_dice_res not in prev_action['match']: 
		if prev_dice_res in prev_action['match']: 
			return action_A
		else:
			return action_B

	else:
		return action_C


def ss1p_29(**kwargs):
	''' Down the stakes if success in previous round, up the stakes otherwise'.
	If profit_own==9, choose B. If profit==10, choose C. Start with A'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']
	prev_ix = actions.index(prev_action)
	
	if throws==0:
		return action_A
	elif profit==9:
		return action_B
	elif profit==10:
		return action_C
	elif prev_dice_res in prev_action['match']: ##success
		new_ix = max(prev_ix-1,0)
		return actions[new_ix]
	else:
		new_ix = min(prev_ix+1,2)
		return actions[new_ix]

def ss1p_30(**kwargs):
	'''If profit<6 choose B, else choose A'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']
	prev_ix = actions.index(prev_action)
	
	if profit<6:
		return action_B
	else:
		return action_A
	
def ss1p_31(**kwargs):
	'''C,B,A,C,B,C'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']
	prev_ix = actions.index(prev_action)

	if throws==0:
		return action_C
	elif throws==1:
		return action_B
	elif throws==2:
		return action_A
	elif throws==3:
		return action_C
	elif throws==4:
		return action_B
	else:
		return action_C

def ss1p_32(**kwargs):
	''' chooose B or C randomly
	 '''
	return actions[random.randint(1,2)]

def ss1p_33(**kwargs):
	''' Down the stakes if success in previous round,
	 up the stakes otherwise. When profit>=8, choose C'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)
	
	if throws==0:
		return action_B
	elif profit>=8:
		return action_C
	elif prev_dice_res in prev_action['match']: ##success
		new_ix = max(prev_ix-1,0)
		return actions[new_ix]
	else:
		new_ix = min(prev_ix+1,2)
		return actions[new_ix]

def ss1p_34(**kwargs):
	''' AABB'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)
	
	if throws==0:
		counter_A += 1
		return action_A
	elif counter_A<2 and prev_action==action_A:
		counter_A += 1
		return action_A
	elif counter_A>=2 and prev_action==action_A:
		counter_A = 0
		counter_B +=1
		return action_B
	elif counter_B<2  and prev_action==action_B:
		counter_B += 1
		return action_B
	elif counter_B>=2  and prev_action==action_B:
		counter_B = 0
		counter_A += 1
		return action_A

def ss1p_35(**kwargs):
	''' Choose C until 2 points, B until 8 points, then choose C'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if profit<2:
		return action_C
	elif profit<8:
		return action_B
	else:
		return action_C

def ss1p_36(**kwargs):
	''' A,A,C,C,B,B,B,C,C, ....'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if throws<2:
		return action_A
	elif throws<4:
		return action_C
	elif throws<7:
		return action_B
	else:
		return action_C

def ss1p_37(**kwargs):
	''' AAB'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if throws%3==2:
		return action_B
	else:
		return action_A

def ss1p_38(**kwargs):
	'''Start with A. Choose A until fail, then choose B.
	Choose B until fail, then choose C. '''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']

	if throws==0:
		return action_A

	elif prev_action==action_A:
		if prev_dice_res in prev_action['match']: 
			return action_A
		else:
			return action_B

	elif prev_action==action_B and prev_dice_res not in prev_action['match']: 
		if prev_dice_res in prev_action['match']: 
			return action_B
		else:
			return action_C

	else:
		return action_C

def ss1p_39(**kwargs):
	'''If throws<=3 choose B, else choose A'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	profit = kwargs['profit']
	throws = kwargs['throws']
	prev_ix = actions.index(prev_action)

	if throws<3:
		return action_B
	else:
		return action_A

def ss1p_40(**kwargs):
	''' A,A,B,B,B,C,C,C, ....'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if throws<2:
		return action_A
	elif throws<5:
		return action_C
	else:
		return action_C

def ss1p_41(**kwargs):
	''' C,A,B,C ....'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if throws==0:
		return action_C
	elif throws==1:
		return action_A
	elif throws==2:
		return action_B
	else:
		return action_C

def ss1p_42(**kwargs):
	''' B until profit==6, A otherwiaw ....'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if profit<6:
		return action_B
	else:
		return action_A

def ss1p_42(**kwargs):
	''' B until profit==6, A otherwiaw ....'''
	prev_action = kwargs['prev_action']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']
	profit = kwargs['profit']
	prev_ix = actions.index(prev_action)

	if profit==0:
		return action_B
	elif profit==2:
		return action_C
	elif profit==3:
		return action_B
	elif profit==4:
		return action_C
	elif profit==5:
		return action_C
	elif profit==6:
		return action_A
	elif profit==7:
		return action_C
	elif profit==8:
		return action_C
	elif profit==9:
		return action_B
	elif profit==10:
		return action_C


def is_r():
	return actions[random.randint(0,2)] 

''' kwargs = {'profit':profit,'throws':throws, 'prev_action':prev_action,\
					 'prev_dice_res':prev_dice_res}'''

