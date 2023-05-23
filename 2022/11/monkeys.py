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
    'falseMonkeyTarget': falseMonkeyTarget,
    'inspectedItemCount': 0
    }

def doMonkeyInspectItemAt(monkey, i):
  item = monkey['items'][i]
  operator = monkey['operator']
  operand = monkey['operand']

  if operand == 'old': operand = item
  operand = int(operand)

  match operator:
    case '+':
      item += operand
    case '*':
      item *= operand
    case _:
      raise 'no operator match'

  monkey['items'][i] = item // 3

  monkey['inspectedItemCount'] += 1
  return monkey['items'][i]

def doMonkeyTestItem(item: int, testDividend: int, trueMonkeyTarget: int, falseMonkeyTarget: int, monkeys: list):
  if item % testDividend == 0: monkeys[trueMonkeyTarget]['items'].append(item)
  else: monkeys[falseMonkeyTarget]['items'].append(item)

def doRound(monkeys):
  for monkey in monkeys:
    for i, item in list(enumerate(monkey['items']))[::-1]: #iterate backwards to pop off the tail and prevent index out of range
      inspectedItem = doMonkeyInspectItemAt(monkey, i)
      doMonkeyTestItem(inspectedItem, monkey['testDividend'], monkey['trueMonkeyTarget'], monkey['falseMonkeyTarget'], monkeys)
      monkey['items'].pop()
    #monkey['items'] = [] #monkey will throw everything and end up empty handed

def printMonkeys(monkeys):
  for i, monkey in enumerate(monkeys):
    items = monkey['items']
    print(f'Monkey {i}: {monkey}')

def calculateMonkeyBusyness(monkeys):
  def getInspections(monkey):
    return monkey['inspectedItemCount']
  monkeys.sort(reverse=True, key=getInspections)
  if verbosityLevel > 1: printMonkeys(monkeys[0:2])

  return monkeys[0]['inspectedItemCount'] * monkeys[1]['inspectedItemCount']

def main():
  monkeys = []
  monkeyBuffer = []
  with open('input.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        monkeys.append(parseMonkey(monkeyBuffer))
        monkeyBuffer = []
      if verbosityLevel > 1: print(line)

  if verbosityLevel > 1: print(monkeys)
  for r in range(20):
    doRound(monkeys)
  if verbosityLevel > 0: printMonkeys(monkeys)

  print(f'MonkeyBusyness: {calculateMonkeyBusyness(monkeys)}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()