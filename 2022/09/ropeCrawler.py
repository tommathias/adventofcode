#!/usr/bin/python3.10
import numpy

def addCoords(knot, transform):
  knot[0] += transform[0]
  knot[1] += transform[1]

def tailChase(head, tail):
  deltaX = head[0] - tail[0]
  deltaY = head[1] - tail[1]

  if abs(deltaX) == 2 or abs(deltaY) == 2:
    addCoords(tail, [numpy.sign(deltaX), numpy.sign(deltaY)])

def doSteps(count, transform, rope, tailHistory):
  for step in range(count):
    addCoords(rope[0], transform)

    #tailChase the rest of the rope, the last knot can't be chased
    for i in range(len(rope)-1):
      tailChase(rope[i], rope[i+1])
    #build history of tuples to allow hashing to unique set
    tailHistory.append((rope[-1][0], rope[-1][1]))

def doMove(instruction, rope, tailHistory):
  #in format "(U|D|L|R) (/d*)" giving a direction and magnitude
  transforms = {'U': (0,1), 'D': (0, -1), 'L': (-1, 0), 'R': (1,0)}
  parts = instruction.split(' ')
  doSteps(int(parts[1]), transforms[parts[0]], rope, tailHistory)

def main():
  #assume infinite plane
  rope = []
  ropeLength = 10
  for i in range(ropeLength):
    rope.append([0,0])
  tailHistory = []

  with open('input.txt') as f:
    for line in f:
      doMove(line, rope, tailHistory)

  #only unique values from history
  print(len(set(tailHistory)))
  print('Thank you for playing Wing Commander')

if __name__ == '__main__':
  main()
