#!/usr/bin/python3
def isVisibleN(x, y, forest):
  h = forest[y][x]
  for i in range(y-1, -1, -1): #lower range is -1 due to 0 based index
    if(forest[i][x] >= h):
      return False
  return True

def isVisibleE(x, y, forest):
  limit = len(forest[y])
  h = forest[y][x]
  for i in range(x+1, limit, 1):
    if(forest[y][i] >= h):
      return False
  return True

def isVisibleS(x, y, forest):
  limit = len(forest)
  h = forest[y][x]
  for i in range(y+1, limit, 1):
    if(forest[i][x] >= h):
      return False
  return True

def isVisibleW(x, y, forest):
  h = forest[y][x]
  for i in range(x-1, -1, -1): #lower range is -1 due to 0 based index
    if(forest[y][i] >= h):
      return False
  return True

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

visibleCount = 0
pointerY = 0
for row in forest:
  pointerX = 0
  for tree in row:
    #python short-circuits boolean logic
    if (isVisibleN(pointerX, pointerY, forest) or
    isVisibleE(pointerX, pointerY, forest) or
    isVisibleS(pointerX, pointerY, forest) or
    isVisibleW(pointerX, pointerY, forest)):
      visibleCount +=1
    pointerX+=1
  pointerY+=1

print(f'{visibleCount} tree(s) visible')