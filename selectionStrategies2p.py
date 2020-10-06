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

def ss2p_f(**kwargs):
	'''flip'''
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		prev_action_own = kwargs['prev_action_p1']
	else:
		prev_action_own = kwargs['prev_action_p2']

	if prev_action_own == action_A:
		return action_B
	elif prev_action_own == action_B:
		return action_C
	else:
		return action_A

def ss2p_1(**kwargs):
	''' Reinforcement learning based ....'''
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own==0:
		return action_B
	elif profit_own==2:
		return action_C
	elif profit_own==3:
		return action_B
	elif profit_own==4:
		return action_C
	elif profit_own==5:
		return action_C
	elif profit_own==6:
		return action_A
	elif profit_own==7:
		return action_C
	elif profit_own==8:
		return action_C
	elif profit_own==9:
		return action_B
	elif profit_own==10:
		return action_C

def ss2p_2(**kwargs):
	''' use strategy B to reach 6 points. Else, action_A'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_B
	else:
		return action_A

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
	else:
		return action_C

def ss2p_5(**kwargs):
	'''Start at C. If I get pt and 2nd didn’t get pt then I go down. 
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
	throws = kwargs['throws']

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
	if throws ==0:
		new_ix = 2 #C index
	elif own_win and not opp_win:
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
	elif profit_own >=6:
		return action_B


def ss2p_10(**kwargs):
	'''Play B 2 in a row, then A 2 in a row'''
	#get kwargs
	global counter_B,counter_A
	throws = kwargs['throws']

	#return action according to profit
	if throws==0:
		counter_B = 1
		counter_A = 0
		return action_B

	elif count_B < 2:
		count_A = 0
		count_B += 1
		return action_B

	elif count_B >= 2:
		count_B = 0
		count_A += 1
		return action_A

def ss2p_11(**kwargs):
	'''PRandom action if score<8. If diff == 5, choose A.
	 If distance == 8, action_C. If distance ==9, action_C.'''
	#get kwargs

	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own
	#return action according to profit
	if diff > 5:
		return action_A
	elif profit_own < 8:
		return actions[random.randint(0,2)] 
	elif profit_own == 8:
		return action_C
	elif profit_own == 9:
		return action_B
	elif profit_own >=10:
		return action_C

def ss2p_12(**kwargs):
	'''C while diff<0 or profit_own==0. B if diff>=0 . 
	A if profit_own == 6. C if profit_own==10.'''
	#get kwargs

	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own
	#return action according to profit
	if diff < 0 or profit_own==0:
		return action_C
	elif profit_own == 6:
		return action_A
	elif diff >= 0:
		return action_B
	elif profit_own == 9:
		return action_B
	elif profit_own >=10:
		return action_C

def ss2p_13(**kwargs):
	''' use strategy A to reach 6 points,then use strategy C.'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_A
	else:
		return action_C

def ss2p_14(**kwargs):
	''' use strategy A to reach 6 points. If profit_opp>=9, action_A.
	If profit_opp>9, action_C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_A
	elif profit_opp>=9:
		return action_A
	elif profit_opp<9:
		return action_C
	else:
		return action_C


def ss2p_15(**kwargs):
	''' if diff<0, action_A, if diff==0, action_B, if diff>0, action_C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own

	if diff<0:
		return action_A
	elif diff==0:
		return action_B
	elif diff>0:
		return action_C

def ss2p_16(**kwargs):
	''' use strategy B to reach 6 points,then use strategy A.'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_B
	else:
		return action_A

def ss2p_17(**kwargs):
	''' use strategy C to reach 6 points,then use strategy C.'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own
	if profit_own<6:
		return action_C
	elif diff<2:
		return action_B
	elif diff>=2:
		return action_A
	else:
		return action_C

def ss2p_18(**kwargs):
	''' use strategy B to reach twice,then use strategy C.'''
		#get kwargs
	throws = kwargs['throws']

	if throws<2:
		return action_B
	else:
		return action_C

def ss2p_19(**kwargs):
	''' use strategy A once,then use strategy B twice, then A.'''
		#get kwargs
	throws = kwargs['throws']

	if throws<1:
		return action_A
	elif throws<3:
		return action_B
	else:
		return action_A
		
def ss2p_20(**kwargs):
	''' use strategy B,C,B,A,A,C,C,C'''
		#get kwargs
	throws = kwargs['throws']

	if throws==0 or 2:
		return action_B
	elif throws==1:
		return action_C
	elif throws==3 or throws==4:
		return action_B
	else:
		return action_A
		
def ss2p_21(**kwargs):
	''' Choose C until 2 points, then A until 8, then C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<2:
		return action_C
	elif profit_own<8:
		return action_A
	else:
		return action_C

def ss2p_22(**kwargs):
	''' Choose B until profit==2, A until profit==9, then B'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<3:
		return action_B
	elif profit_own<9:
		return action_A
	else:
		return action_B

def ss2p_23(**kwargs):
	''' Choose C until profit==2, B until profit==8, then C
	choose A  if diff>4????'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own
	if diff>4:
		return action_A
	elif profit_own<2:
		return action_C
	elif profit_own<8:
		return action_B
	else:
		return action_C

def ss2p_24(**kwargs):
	''' Choose C until profit==6, B until profit==8, then B once more
	choose A  afterwards????'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']

	if profit_own<6:
		return action_C
	elif profit_own<9:
		return action_B
	elif profit_own<12 and prev_dice_res in prev_action['match']:
		return action_B
	else:
		return action_C

def ss2p_25(**kwargs):
	''' If profit_opp<6: if profit_own<7 , choose action_A,
	 if profit_own==7 choose action_B, else choose action_C
	If profit_opp>=6: Choose B until profit ==6, choose C otherwise. '''
	global counter_B,counter_A

	#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	if throws ==0:
		counter_B = 0

	if profit_opp >=6:
		if profit_own<7:
			conter_B = 0
			return action_A
		elif profit_own == 7 and counter_B<2:
			counter_B += 1
			return action_B
		else:
			counter_B = 0
			return action_C

	else:
		if profit_own>6 or throws>=4:
			return action_C
		else:
			return action_B

def ss2p_26(**kwargs):
	''' Start with B. If prrofit_opp<=0, action_A.
	If diff>=3, profit_own>=10 or else action_C.
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if throws==0:
		return action_B
	elif profit_opp<=0 and throws>1:
		return action_A
	elif diff>=3:
		return action_C
	elif profit_own>=10:
		return action_C
	else:
		return action_C

def ss2p_27(**kwargs):
	''' Start with B. If prrofit_opp<=0, action_A.
	If diff>=3, profit_own>=10 or else action_C.
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if throws==0:
		return action_B
	elif profit_opp<=0 and throws>1:
		return action_A
	elif diff>=3:
		return action_C
	elif profit_own>=10:
		return action_C
	else:
		return action_C

def ss2p_28(**kwargs):
	''' Choose A. If diff>=0 and profit_own==10, choose C, if profit_own==9
	choose B, else choose A.  
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if diff<0 and profit_own<9:
		return action_A
	elif diff<0 and profit==9:
		return action_B
	elif diff<0 and profit>9:
		return action_C
	else:
		return action_A

def ss2p_29(**kwargs):
	''' Begin with two As. Choose action B unless profit_opp>=9. 
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if throws==0 or throws==1:
		return action_A
	elif profit_opp>=9:
		return action_A
	else:
		return action_B


def ss2p_30(**kwargs):
	''' If profit_own<6, choose action C. Else if profit_own>=6,
	try B once. If success, keep choosing B, else choose A. 
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if profit_own<6:
		return action_C
	elif profit_own>=6 and prev_action == action_C:
		return action_B
	elif profit_own>=6 and prev_action == action_B:
		if prev_dice_res in prev_action['match']:
			return action_B
		else:
			return action_A
	else:
		return action_A

def ss2p_31(**kwargs):
	''' B,C,C,C,C,B 
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

	diff = profit_opp - profit_own

	if throws==0:
		return action_B
	elif profit_own<9:
		return action_C
	else:
		return action_B

def ss2p_32(**kwargs):
	''' chooose B or C randomly
	 '''
	return actions[random.randint(1,2)]

def ss2p_33(**kwargs):
	''' B,C,C,C,C,B 
	 '''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
		prev_action = kwargs['prev_action_p1']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
		prev_action = kwargs['prev_action_p2']
	prev_dice_res = kwargs['prev_dice_res']
	throws = kwargs['throws']

def ss2p_34(**kwargs):
	''' use strategy A to reach 6 points,then use strategy B.'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_A
	else:
		return action_B

def ss2p_35(**kwargs):
	''' use strategy C to reach 2 points,then use strategy B
	to reach 8 points, then choose C.'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<2:
		return action_C
	elif profit_own<8:
		return action_B
	else:
		return action_C


def ss2p_36(**kwargs):
	''' use strategy a unless probability oof winning is low'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own

	if diff > 4 :
		return action_A
	else:
		return action_B

def ss2p_37(**kwargs):
	'''AAB'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']
	throws = kwargs['throws']

	if throws%3==2:
		return action_B
	else:
		return action_A

def ss2p_38(**kwargs):
	''' if diff==0, action_A, else choose C or B at random'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	diff = profit_opp - profit_own

	if diff==0:
		return actions[random.randint(1,2)]
	else:
		return action_A

def ss2p_39(**kwargs):
	''' iAABBBCCC'''
		#get kwargs		
	throws = kwargs['throws']

	if throws<2:
		return action_A
	elif throws<5:
		return action_C
	else:
		return action_C

def ss2p_40(**kwargs):
	''' AAABCB'''
		#get kwargs		
	throws = kwargs['throws']

	if throws<3:
		return action_A
	elif throws==3:
		return action_B
	elif throws==4:
		return action_C
	else:
		return action_B

def ss2p_41(**kwargs):
	''' use strategy A to reach 6 points.Else, action_B'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_A
	else:
		return action_B

def ss2p_42(**kwargs):
	''' use strategy A to reach 6 points. Else, action_C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_A
	else:
		return action_C

def ss2p_43(**kwargs):
	''' use strategy C to reach 6 points. Else, action_A'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_C
	else:
		return action_A

def ss2p_44(**kwargs):
	''' use strategy C to reach 6 points. Else, action_B'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_C
	else:
		return action_B

def ss2p_46(**kwargs):
	''' use strategy B to reach 6 points. Else, action_C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<6:
		return action_B
	else:
		return action_C

def ss2p_47(**kwargs):
	''' use strategy B to reach 6 points. Else, action_C'''
		#get kwargs
	whoAmI = kwargs['whoAmI']
	if whoAmI == 'p1':
		profit_own = kwargs['profit_p1']
		profit_opp = kwargs['profit_p2']
	else:
		profit_own = kwargs['profit_p2']
		profit_opp = kwargs['profit_p1']

	if profit_own<2:
		return action_C
	if profit_own<5:
		return action_B
	else:
		return action_A

def is_r():
	return actions[random.randint(0,2)] 


'''args_p2 = {'profit_p1':profit_p1,'profit_p2':profit_p2,\
			  'throws':throws, 'prev_action_p1':prev_action_p1,\
			  'prev_action_p2':prev_action_p2,\
			  'prev_dice_res':prev_dice_res,\
			  'sel_action_p1':sel_action_p1}'''