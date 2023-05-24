def parseFactor(monkeyBuffer):
  factor = monkeyBuffer[2].split(':')[1].split(' ')[5].strip()
  if factor == 'old': return
  return int(factor)

def main():
  monkeyBuffer = []
  testFactors = []
  inputFactors = []

  with open('test.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        testFactors.append(parseFactor(monkeyBuffer))
        monkeyBuffer = []
  f.close()

  with open('input.txt') as f:
    for line in f:
      monkeyBuffer.append(line)
      if len(monkeyBuffer) == 7:
        inputFactors.append(parseFactor(monkeyBuffer))
        monkeyBuffer = []
  f.close()

  with open('factors.txt', 'w') as f:
    f.write(f'test.txt factors: {set(testFactors)}')
    f.write(f'input.txt factors: {set(inputFactors)}')

if __name__ == '__main__': main()