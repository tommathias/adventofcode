#!/usr/bin/python3.10
import monkeys as monkeyPy
import math
import cProfile
from progress.bar import Bar
import primefac

verbosityLevel = 0
shouldProfile = False


# monkey items are stored as a collection of their prime factors
# factors must be split into their prime factors

def factorise(n: str):
  if verbosityLevel > 0: print(f'factorise({n})')
  if n == 'old': return []
  return list(primefac.primefac(int(n)))

def monkeySquare(item: list):
  if verbosityLevel > 0: print(f'monkeySquare({item})')
  #we already have the prime factors for the number, add them
  item = item + item
  return item

def monkeyMultiply(item: list, multiplcand: list):
  if verbosityLevel > 0: print(f'monkeyMultiply({item})')
  item.extend(multiplcand)
  return item

def monkeyAdd(item: list, addend: int):
  if verbosityLevel > 0: print(f'monkeyAdd({item, addend})')
  #multiply, add, refactor
  n = math.prod(item)
  n += addend

  return factorise(n)

# def monkeySee():
#   monkeyDo()

def doMonkeyInspectFactorisedItemAt(monkey, i: int):
  monkey['inspectedItemCount'] += 1

  factorisedItem = monkey['factorisedItems'][i]
  operator = monkey['operator']
  operand = monkey['operand']

  if operand == 'old':
    factorisedItem = monkeySquare(factorisedItem)
    return factorisedItem

  match operator:
    case '+':
      return factorisedItem
      factorisedItem = monkeyAdd(factorisedItem, int(operand))
    case '*':
      factorisedItem = monkeyMultiply(factorisedItem, monkey['fOperand'])
    case _:
      raise 'no operator match'

  return factorisedItem

def doMonkeyTestFactorisedItem(factorisedItem: list, monkey, monkeys: list):
  testDividend = monkey['testDividend']
  trueMonkeyTarget = monkey['trueMonkeyTarget']
  falseMonkeyTarget = monkey['falseMonkeyTarget']

  if testDividend in factorisedItem:
    factorisedItem.remove(testDividend)
    monkeys[trueMonkeyTarget]['factorisedItems'].append(factorisedItem)
  else:
    monkeys[falseMonkeyTarget]['factorisedItems'].append(factorisedItem)

def doFactorisedRound(monkeys):
  for monkey in monkeys:
    for i in range(len(monkey['factorisedItems']))[::-1]: #iterate backwards to pop off the tail and prevent index out of range
      inspectedItem = doMonkeyInspectFactorisedItemAt(monkey, i)
      doMonkeyTestFactorisedItem(inspectedItem, monkey, monkeys)
      monkey['factorisedItems'].pop()

def main():
  monkeys = []
  monkeyBuffer = []

  with open('input.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        mf = monkeyPy.parseMonkey(monkeyBuffer)

        mf['fOperand'] = factorise(mf['operand'])
        mf['factorisedItems'] = []

        for item in mf['items']:
          mf['factorisedItems'].append(factorise(item))

        monkeys.append(mf)
        monkeyBuffer = []
      if verbosityLevel > 1: print(line)

  if verbosityLevel > 1: print(monkeys)
  rounds = 10
  bar = Bar('Processing', max= rounds)
  for r in range(rounds):
    doFactorisedRound(monkeys)
    bar.next()
  bar.finish()
  if verbosityLevel > 1: monkeyPy.printMonkeys(monkeys)

  print(f'MonkeyBusyness: {monkeyPy.calculateMonkeyBusyness(monkeys)}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__':
  cProfile.run('main()') if shouldProfile else main()
  #N.B. test.txt for 20 rounds should return 10197