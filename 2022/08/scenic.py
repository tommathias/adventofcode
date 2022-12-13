#!/usr/bin/python3
def getScoreN(x, y, forest):
  scoreN = 0
  h = forest[y][x]
  for i in range(y-1, -1, -1): #lower range is -1 due to 0 based index
    scoreN += 1
    if(forest[i][x] >= h):
      return scoreN
  return scoreN

def getScoreE(x, y, forest):
  scoreE = 0
  limit = len(forest[y])
  h = forest[y][x]
  for i in range(x+1, limit, 1):
    scoreE += 1
    if(forest[y][i] >= h):
      return scoreE
  return scoreE

def getScoreS(x, y, forest):
  scoreS = 0
  limit = len(forest)
  h = forest[y][x]
  for i in range(y+1, limit, 1):
    scoreS += 1
    if(forest[i][x] >= h):
      return scoreS
  return scoreS

def getScoreW(x, y, forest):
  scoreW = 0
  h = forest[y][x]
  for i in range(x-1, -1, -1): #lower range is -1 due to 0 based index
    scoreW += 1
    if(forest[y][i] >= h):
      return scoreW
  return scoreW

forest = []
with open('input.txt') as f:
  for line in f:
    line = line.strip()
    row = []
    for char in line:
      row.append(char)
    forest.append(row)

#N.B. because forest is built row by row, co-ordinates are forest[y][x]
#print(forest)

highScore = 0
pointerY = 0
for row in forest:
  pointerX = 0
  for tree in row:
    score = getScoreN(pointerX, pointerY, forest) * getScoreE(pointerX, pointerY, forest) * getScoreS(pointerX, pointerY, forest) * getScoreW(pointerX, pointerY, forest)
    #print(f'({pointerX}, {pointerY}) score: {score}')
    if (score > highScore):
      highScore = score
    pointerX+=1
  pointerY+=1

print(f'Highest scenic score: {highScore}')