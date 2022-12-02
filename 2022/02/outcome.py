#!/usr/bin/python3
total = 0

#create a matrix of precalculated scores for a given throw and its result
#ROCK/A = 1, PAPER/B = 2, SCISSORS/C = 3
#LOSE/X = 0, DRAW/Y = 3, WIN/Z = 6
outcomeMatrix = {
  'A': { 'X': 3, 'Y': 4, 'Z': 8}, #15
  'B': { 'X': 1, 'Y': 5, 'Z': 9}, #15
  'C': { 'X': 2, 'Y': 6, 'Z': 7} #15
}


with open('input.txt') as f:
  for line in f:
    them = line[0]
    result = line[2]

    total += outcomeMatrix[them][result]

print(total)