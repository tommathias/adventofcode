#!/usr/bin/python3.10
loggingLevel = 1

def tailChase(head, tail):
  #check if tail needs to catch up
  #2 away orthagonally
  deltaX = head[0] - tail[0]
  deltaY = head[1] - tail[1]
  if deltaX == 2:
    tail[0] = head[0]-1
    tail[1] = head[1]
  if deltaX == -2:
    tail[0] = head[0]+1
    tail[1] = head[1]
  if deltaY == 2:
    tail[0] = head[0]
    tail[1] = head[1]-1
  if deltaY == -2:
    tail[0] = head[0]
    tail[1] = head[1]+1

def printCoords(head, tail):
  print(f'head at {head} tail at {tail}')

def doSteps(count, transform, head, tail, tailHistory):
  #number of steps, transform in format [x,y]
  for step in range(count):
    head[0] += transform[0]
    head[1] += transform[1]
    tailChase(head, tail)
    if loggingLevel > 0 : printCoords(head, tail)
    #build history of tuples to allow hashing to unique set
    tailHistory.append((tail[0], tail[1]))

def doMove(instruction, head, tail, tailHistory):
  #in format "U|D|L|R (/d*) giving a direction and magnitude
  match instruction.split(' '):
    case 'U', mag:
      doSteps(int(mag), (0, 1), head, tail, tailHistory)
    case 'D', mag:
      doSteps(int(mag), (0, -1), head, tail, tailHistory)
    case 'L', mag:
      doSteps(int(mag), (-1, 0), head, tail, tailHistory)
    case 'R', mag:
      doSteps(int(mag), (1, 0), head, tail, tailHistory)
    case _:
      raise('no line match')

def main():
  #assume infinite plane
  #store coords in tuples
  head = [0,0]
  tail = [0,0]
  tailHistory = []
  printCoords(head, tail)

  with open('test.txt') as f:
    for line in f:
      if loggingLevel > 1: print(line)
      doMove(line, head, tail, tailHistory)

  historySet = set(tailHistory)
  print(historySet)
  print(len(historySet))
  print('Thank you for playing Wing Commander')

main()
