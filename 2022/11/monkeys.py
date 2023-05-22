#!/usr/bin/python3.10
verbosityLevel = 1

def parseMonkey(monkeyBuffer):
  items = list(map(int, monkeyBuffer[1].split(':')[1].split(','))) #py3 map(fn, []) returns lazy object, get values with list()
  operation = monkeyBuffer[2].split(':')[1].split(' ')
  testDividend = int(monkeyBuffer[3].split(' ')[-1])
  trueMonkeyTarget = int(monkeyBuffer[4].split(' ')[-1])
  falseMonkeyTarget = int(monkeyBuffer[5].split(' ')[-1])
  return {
    'items': items,
    'operator': operation[4],
    'operand': operation[5].strip(),
    'testDividend': testDividend,
    'trueMonkeyTarget': trueMonkeyTarget,
    'falseMonkeyTarget': falseMonkeyTarget
    }

def doMonkeyInspectItem(operator: str, operand: str, item: int):
  if operand == 'old': operand = item
  operand = int(operand)

  match operator:
    case '+':
      item += operand
    case '*':
      item *= operand
    case _:
      raise 'no operator match'

  item = item // 3

def doMonkeyTestItem(item: int, testDividend: int, trueMonkeyTarget: int, falseMonkeyTarget: int, monkeys: list):
  if item % testDividend == 0: monkeys[trueMonkeyTarget].append(item)
  else: monkeys[falseMonkeyTarget].append(item)

def doRoundOne(monkeys):
  for monkey in monkeys:
    for item in monkey['items']:
      doMonkeyInspectItem(monkey['operator'], monkey['operand'], item)
    #monkey['items'] = [] #monkey will throw everything and end up empty handed

def main():
  monkeys = []
  monkeyBuffer = []
  with open('test.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        monkeys.append(parseMonkey(monkeyBuffer))
        monkeyBuffer = []
      if verbosityLevel > 1: print(line)

  if verbosityLevel > 0: print(monkeys)
  doRoundOne(monkeys)
  print(monkeys)
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()