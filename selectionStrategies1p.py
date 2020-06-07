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
    
def ss1p_5(**kwargs):
    global counter
    counter +=1
    if counter%2 == 0:
        return action_A
    else:
        return action_B
    
def ss1p_6(**kwargs):
    global counter
    counter +=1
    if counter%2 == 0:
        return action_A
    else:
        return action_C

def ss1p_7(**kwargs):
    global counter
    counter +=1
    if counter%2 == 0:
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
    profit = kwargs['profit']
    if profit < 6:
        return action_B
    else:
        return action_C

def ss1p_12(**kwargs):
    ''' Down the stakes if success in previous round, up the stakes otherwise'''
    prev_action = kwargs['prev_action']
    prev_dice_res = kwargs['prev_dice_res']
    prev_ix = actions.index(prev_action)
    
    if prev_dice_res in prev_action['match']: ##success
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
    if profit_own < 6:
        return action_A
    elif profit_own >6:
        return action_B

        
def is_a():
    return action_A

def is_b():
    return action_B

def is_c():
    return action_C

def is_r():
    return actions[random.randint(0,2)] 

''' kwargs = {'profit':profit,'throws':throws, 'prev_action':prev_action,\
                     'prev_dice_res':prev_dice_res}'''

