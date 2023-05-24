#!/usr/bin/python3.10
from progress.bar import Bar
import cProfile

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

def doMonkeyInspectItemAt(monkey, i: int, worryFactor: int):
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

  if worryFactor != 1:
    newWorry = item // worryFactor
  else:
    #N.B. without reducing worry, the worry grows geometrically
    # Need a new approach for storing large numbers, potentially as collections of factors?
    newWorry = item

  monkey['inspectedItemCount'] += 1
  return newWorry

def doMonkeyTestItem(item: int, monkey, monkeys: list):
  testDividend = monkey['testDividend']
  trueMonkeyTarget = monkey['trueMonkeyTarget']
  falseMonkeyTarget = monkey['falseMonkeyTarget']

  if item % testDividend == 0:
    monkeys[trueMonkeyTarget]['items'].append(item)
  else:
    monkeys[falseMonkeyTarget]['items'].append(item)

def doRound(monkeys, worryFactor: int):
  for monkey in monkeys:
    for i in range(len(monkey['items']))[::-1]: #iterate backwards to pop off the tail and prevent index out of range
      inspectedItem = doMonkeyInspectItemAt(monkey, i, worryFactor)
      doMonkeyTestItem(inspectedItem, monkey, monkeys)
      monkey['items'].pop()

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
  worryFactor = 1

  with open('input.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        monkeys.append(parseMonkey(monkeyBuffer))
        monkeyBuffer = []
      if verbosityLevel > 1: print(line)

  if verbosityLevel > 1: print(monkeys)
  rounds = 10_000
  bar = Bar('Processing', max= rounds)
  for r in range(rounds):
    doRound(monkeys, worryFactor)
    bar.next()
  bar.finish()
  if verbosityLevel > 1: printMonkeys(monkeys)

  print(f'MonkeyBusyness: {calculateMonkeyBusyness(monkeys)}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__':
  cProfile.run('main()')