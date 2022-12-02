#!/usr/bin/python3
total = 0

verbose = False
#To save nested ifs or matches, rationalise the outcome based on the score
#for each type. If a and b both throw the same thing, a-b==0.
#See whether other sums aligns for win/lose
#ROCK = 1, PAPER = 2, SCISSORS = 3
#vs outcome minus
# 1,1 D 0
# 1,2 L -1
# 1,3 W -2
# 2,1 W 1
# 2,2 D 0
# 2,3 L -1
# 3,1 L 2
# 3,2 W 1
# 3,3 D 0

# they do
# -2 W
# -1 LL
# 0 DDD
# 1 WW
# 2 L

#could do something bitwise, but can add an offset add resulting win/lose/draw points
#into a list

# 0 W
# 1 L
# 2 D
# 3 W
# 4 L

#points for win=6, draw=3, lose=0
#A=ROCK, B=PAPER, C=SCISSORS
#X=ROCK, Y=PAPER, Z=SCISSORS
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
resultPoints = [6,0,3,6,0]


with open('input.txt') as f:
  for line in f:
    me = points[line[2]]
    if verbose: print(f'me:{me}')
    them = points[line[0]]
    if verbose: print(f'them:{them}')

    result = me-them
    if verbose: print(f'result:{result}')
    if verbose: print(f'+=offset:{result+2}')
    score = resultPoints[result+2] #offset
    if verbose: print(f'score:{score}')
    total += me + score
    if verbose: print(f'total: {total}')
    if verbose: print('---')

print(total)