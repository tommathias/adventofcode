#!/usr/bin/python3.10
import os
import time
import numpy

loggingLevel = 1
screenMode = 'draw'
redrawFrequency = 'step'
refreshMode = 'manual'

def tailChase(head, tail):
  #situations         deltas                                transforms
  # [H][H][H][H][H]   [-2, 2][-1, 2][ 0, 2][ 1, 2][ 2, 2]   [-1, 1][-1, 1][ 0, 1][ 1, 1][ 1, 1]
  # [H][.][.][.][H]   [-2, 1]                     [ 2, 1]   [-1, 1]                     [ 1, 1]
  # [H][.][T][.][H]   [-2, 0]                     [ 2, 0]   [-1, 0]                     [ 1, 0]
  # [H][.][.][.][H]   [-2,-1]                     [ 2,-1]   [-1,-1]                     [ 1,-1]
  # [H][H][H][H][H]   [-2,-2][-1,-2][ 0,-2][ 1,-2][ 2,-2]   [-1,-1][-1,-1][ 0,-1][ 1,-1][ 1,-1]

  #notice the transforms are same as deltas with magnitude of 1

  #check if tail needs to catch up
  deltaX = head[0] - tail[0]
  deltaY = head[1] - tail[1]

  if abs(deltaX) == 2 or abs(deltaY) == 2:
    tail[0] += numpy.sign(deltaX)
    tail[1] += numpy.sign(deltaY)

def updateScreen(rope):
  if loggingLevel > 0 and screenMode == 'print': printCoords(rope)
  if loggingLevel > 0 and screenMode == 'draw': drawCoords(rope)

def drawCoords(rope):
  clear = lambda: os.system('clear')
  clear()

  resolutionx = 50
  resolutiony = 20
  xoffset = resolutionx/2
  yoffset = resolutiony/2
  originoffset = 1
  for y in reversed(range(resolutiony+originoffset)):
    xBuffer = ''
    for x in range(resolutionx+originoffset):
      topknot = '.'
      if x == xoffset and y == yoffset:
        topknot = 's'
      for i, knot in reversed(list(enumerate(rope))):
        if knot[0] == x-xoffset and knot[1] == y-yoffset:
          topknot = str(i)
          if i == 0:
            topknot = 'H'
      xBuffer += topknot
    print(xBuffer)
  if refreshMode == 'manual': input('Press enter for next step')

def printCoords(rope):
  print(rope)

def doSteps(count, transform, rope, tailHistory):
  #number of steps, transform in format [x,y]
  for step in range(count):
    rope[0][0] += transform[0]
    rope[0][1] += transform[1]
    if redrawFrequency == 'step': updateScreen(rope)

    #tailChase the whole rope
    for i in range(len(rope)-1):
      tailChase(rope[i], rope[i+1])
      if redrawFrequency == 'step': updateScreen(rope)
    #build history of tuples to allow hashing to unique set
    tailHistory.append((rope[-1][0], rope[-1][1]))
    if screenMode == 'print': print('=====')

def doMove(instruction, rope, tailHistory):
  #in format "U|D|L|R (/d*) giving a direction and magnitude
  match instruction.split(' '):
    case 'U', mag:
      doSteps(int(mag), (0, 1), rope, tailHistory)
    case 'D', mag:
      doSteps(int(mag), (0, -1), rope, tailHistory)
    case 'L', mag:
      doSteps(int(mag), (-1, 0), rope, tailHistory)
    case 'R', mag:
      doSteps(int(mag), (1, 0), rope, tailHistory)
    case _:
      raise('no line match')
  if redrawFrequency == 'move': updateScreen(rope)
  if refreshMode == 'auto': time.sleep(1)
  if screenMode == 'print': print('=====')

def main():
  #assume infinite plane
  #store coords in tuples
  rope = []
  ropeLength = 10
  for i in range(ropeLength):
    rope.append([0,0])
  tailHistory = []
  updateScreen(rope)

  with open('input.txt') as f:
    for line in f:
      if loggingLevel > 1: print(line)
      doMove(line, rope, tailHistory)

  historySet = set(tailHistory)
  print(historySet)
  print(len(historySet))
  print('Thank you for playing Wing Commander')

main()
