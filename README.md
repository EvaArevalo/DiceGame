A dice game for the class Science Encountered-Time, evolution, and Decisions, and tackles decision making under uncertainty. 

PROBLEM INSTRUCTIONS:

In a game of dice, there are three options for the player to choose. 
(r= reward, p=probability, D=outcome of throwing a dice)
A: r=6, p=1/6, D=1
B: r=3, p=1/3, D=2 or 3
C: r=2, p=1/2, D=4, 5, or 6.
Goal=12

The player that reaches the goal within the least times wins.
The player should choose A, B, or C, then throws the dice.
For example, a player throws a dice, with the outcomes as below:
Round 1: choose A, throwing the dice with an outcome of 2 (2 <>D=1, fail), staying at 0.
Round 2: choose B, throwing the dice with an outcome of 2 (2 =D=2, success), going to 3.
Round 3: choose A, throwing the dice with an outcome of 1 (1 = D=1, success), going to 6+3=9.
Round 4: choose B, throwing the dice with an outcome of 4 (4 <> D=2, fail), staying at 9.
Round 5: choose B, throwing the dice with an outcome of 3 (3 = D=3, success), going to 3+9=12.
Reach the goal and end the game.

Please provide your strategy to win this game for a single player as well as for 2 players.

Important Note: A strategy should contain your reasoning for making your choices. Your strategy should not apply to only one example. If you don't provide a reasoning, your submission strategy is the same as a random strategy.

DIRECTORY:

A discussion on how to solve this problem is provided in the file:
'Science encountered sol - Eva.docx'

Student strategies for the single player version can be found in the file: 'selectionStrategies1p.py'

Student strategies for the 2 playerw version can be found in the file: 'selectionStrategies2p.py'

A reinforcement learning solution using OpenAI's Gym library for Python is provided in the file:
'ScienceGEClass_HW.ipynb' (under the ‘Reinforcement learning’ section)

HOW TO RUN:

In the console, after entering the program, we can enter a student id (or 2) and get the simulation result.

To play 1 player game, type at the bottom:
python playSingle.py

To play 2 player game, type:
python play2players.py

To stop the program, type:
Ctrl+Z

