#!/usr/bin/python3
loggingLevel = 1

def renderPixel(state):
  resolution = 40
  beam = state['cycle']%resolution
  if state['X']-1 == beam or state['X'] == beam or state['X']+1 == beam:
    state['buffer'] += '#'
  else:
    state['buffer'] += '.'

def calculateSignalStrength(state):
  return state['X'] * state['cycle']

def runCyclePart1(state):
  state['cycle']+=1
  if loggingLevel > 0: print(state)
  if state['cycle'] in state['interestingCycles']:
    state['runningSignalStrength'] += calculateSignalStrength(state)

def runCyclePart2(state):
  renderPixel(state)
  state['cycle']+=1
  if loggingLevel > 1: print(state)

def runCycle(state):
  if 'runningSignalStrength' in state: runCyclePart1(state)
  else: runCyclePart2(state)

def draw(state):
  print(state['buffer'][0:39])
  print(state['buffer'][40:79])
  print(state['buffer'][80:119])
  print(state['buffer'][120:159])
  print(state['buffer'][160:199])
  print(state['buffer'][200:239])

def main():
  with open('input.txt') as f:
    state1 = { 'X': 1, 'cycle': 0, 'interestingCycles': [20,60,100,140,180,220], 'runningSignalStrength': 0 }
    state2 = { 'X': 1, 'cycle': 0, 'buffer':'' }

    state = state1

    if loggingLevel > 0: print(f'initial state: {state}')

    for line in f:
      match line.split():
        case ['noop']:
          runCycle(state)
        case ['addx', n]:
          runCycle(state)
          runCycle(state)
          state['X']+=int(n)
        case [_]:
          print(line)
          raise('no line match')
  if loggingLevel > 0: print(f'final state: {state}')
  if 'buffer' in state: draw(state)

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
