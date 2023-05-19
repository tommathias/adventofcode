#!/usr/bin/python3.10
loggingLevel = 1

#def moveHead()
def printCoords(head, tail):
    print(f'head at {head} tail at {tail}')

def doSteps(count, transform, head, tail):
  #number of steps, transform in format [x,y]
  for step in range(count):
    head[0] += transform[0]
    head[1] += transform[1]
    if loggingLevel > 0 : printCoords(head, tail)

def doMove(instruction, head, tail):
  #in format "U|D|L|R (/d*) giving a direction and magnitude
  match instruction.split(' '):
    case 'U', mag:
      #transform = [0, int(mag)]
      doSteps(int(mag), [0, 1], head, tail)
    case 'D', mag:
      doSteps(int(mag), [0, -1], head, tail)
    case 'L', mag:
      doSteps(int(mag), [-1, 0], head, tail)
    case 'R', mag:
      doSteps(int(mag), [1, 0], head, tail)
    case _:
      raise('no line match')


def main():
  head = [0,0]
  tail = [0,0]
  printCoords(head, tail)

  with open('test.txt') as f:
    for line in f:
      if loggingLevel > 1: print(line)
      doMove(line, head, tail)
      #printCoords(head, tail)
      #do stuff here
      #assume infinite plane

  print('Thank you for playing Wing Commander')

main()
