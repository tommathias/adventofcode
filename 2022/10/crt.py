#!/usr/bin/python3
loggingLevel = 1

def calculateSignalStrength(state):
  return state['X'] * state['cycle']

def runCycle(state):
  state['cycle']+=1
  if loggingLevel > 0: print(state)
  if state['cycle'] in state['interestingCycles']:
    state['runningSignalStrength'] += calculateSignalStrength(state)

def main():
  with open('input.txt') as f:
    state = { 'X': 1, 'cycle': 0, 'interestingCycles': [20,60,100,140,180,220], 'runningSignalStrength': 0 }
    
    if loggingLevel > 0: print(f'initial state: {state}')
    buffer = []
    for line in f:
      #do stuff here
      #print(line)
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

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
