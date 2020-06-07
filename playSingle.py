import os, sys
from selectionStrategies1p import *
from selectionStrategies2p import *
from diceGameFunctions import *
import diceGameFunctions
import pandas as pd


def play_dice_game_1p_sid(sid,rounds=100):
	'''given sd play n rounds single player game'''
	
	#Raise exception
	if sid not in sid_df['sid'].values:
		print("Unable to call function, ckeck SIDs")
		return
		
	ss1p = sid_df.loc[sid_df['sid']==sid,'ss1p'].values[0]
	if ss1p == 'nan':
		ss1p = ss1p_r
	else:
		ss1p = globals()[ss1p]
	is1p = sid_df.loc[sid_df['sid']==sid,'is1p'].values[0]
	if is1p == 'nan':
		is1p = is_r
	else:
		is1p = globals()[is1p]
	play_dice_game_1p(ss1p,is1p,rounds)

def play_dice_game_2p_sid(sid1,sid2,rounds=100):
	'''given sid1 and sid2 play n rounds 2 player game'''
	
	#Raise exception
	if sid1 not in sid_df['sid'].values or \
	sid2 not in sid_df['sid'].values:
		print("Unable to call function, ckeck SIDs")
		return
	
	#p1
	ss2p_p1 = sid_df.loc[sid_df['sid']==sid1,'ss2p'].values[0]
	if ss2p_p1 == 'nan':
		ss2p_p1 = ss2p_r
	else:
		ss2p_p1 = globals()[ss2p_p1]
	is_p1 = sid_df.loc[sid_df['sid']==sid1,'is2p'].values[0]
	if is_p1 == 'nan':
		is_p1 = is_r
	else:
		is_p1 = globals()[is_p1]
		
	#p2
	ss2p_p2 = sid_df.loc[sid_df['sid']==sid2,'ss2p'].values[0]
	if ss2p_p2 == 'nan':
		ss2p_p2 = ss2p_r
	else:
		ss2p_p2 = globals()[ss2p_p2]
	is_p2 = sid_df.loc[sid_df['sid']==sid2,'is2p'].values[0]
	if is_p2 == 'nan':
		is_p2 = is_r
	else:
		is_p2 = globals()[is_p2]
	
	#if
	if sid_df.loc[sid_df['sid']==sid1,'always_p2'].values[0] == True and \
		sid_df.loc[sid_df['sid']==sid2,'always_p2'].values[0] == True:
		raise Exception
	elif sid_df.loc[sid_df['sid']==sid1,'always_p2'].values[0] == True:
		print('reordering players...')
	tempss = ss2p_p1
	tempis = is_p1
	ss2p_p1 = ss2p_p2
	is_p1 = is_p2
	ss2p_p2 = tempss
	is_p2 = tempis
		
	play_dice_game_2p(ss2p_p1,ss2p_p2,is_p1,is_p2,rounds)   

if __name__ == '__main__':


	sid_df = pd.read_csv('StrategyPerSID.csv')
	sid_df = sid_df.fillna('nan')

	while(True):
		print('***')
		sid = input("Enter a student id: ") 
		sid=int(sid)
		play_dice_game_1p_sid(sid,rounds=1000)
