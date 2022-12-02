#!/usr/bin/python3
total = 0

#To save nested ifs or matches, rationalise the outcome based on the score for each type.
#ROCK = 1, PAPER = 2, SCISSORS = 3
#points for win=6, draw=3, lose=0
#A=ROCK, B=PAPER, C=SCISSORS
#X=ROCK, Y=PAPER, Z=SCISSORS
points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
resultPoints = [6,0,3,6,0]


with open('input.txt') as f:
  for line in f:
    me = points[line[2]]
    them = points[line[0]]
    result = me-them
    score = resultPoints[result+2] #offset
    total += me + score

print(total)