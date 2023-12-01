def parseFactor(monkeyBuffer):
  factor = monkeyBuffer[2].split(':')[1].split(' ')[5].strip()
  if factor == 'old': return
  return int(factor)

def parseDividend(monkeyBuffer):
  dividend = int(monkeyBuffer[3].split(' ')[-1])
  return dividend

def main():
  monkeyBuffer = []
  testFactors = []
  inputFactors = []
  testDividends = []
  inputDividends = []

  with open('test.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        testFactors.append(parseFactor(monkeyBuffer))
        testDividends.append(parseDividend(monkeyBuffer))
        monkeyBuffer = []
  f.close()

  with open('input.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        inputFactors.append(parseFactor(monkeyBuffer))
        inputDividends.append(parseDividend(monkeyBuffer))
        monkeyBuffer = []
  f.close()

  with open('factors.txt', 'w') as f:
    f.write(f'test.txt factors: {set(testFactors)}\n')
    f.write(f'input.txt factors: {set(inputFactors)}\n')
    f.write(f'test.txt Dividends: {set(testDividends)}\n')
    f.write(f'input.txt Dividends: {set(inputDividends)}\n')

if __name__ == '__main__': main()