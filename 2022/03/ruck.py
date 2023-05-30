#!/usr/bin/python3
def getPriority(char):
  if not char.isalpha():
    raise('Can only prioritise letters')

  cOrd = ord(char)
  if(cOrd > 96): #lower
    return cOrd-96
  if(cOrd > 64): #upper
    return cOrd-38
  raise('You werent supposed to be able to get here you know')

def main():
  compartmentN = 2
  total = 0

  with open('input.txt') as f:
    for line in f:
      line = line.strip() #remove \n
      #print(line)
      #split line into n=2 compartments
      itemCount = len(line)
      compartmentSize = itemCount/compartmentN

      bag = []
      for i in range(compartmentN):
        start = int(i*compartmentSize)
        end = int(start+compartmentSize)
        contents = line[start:end]
        bag.append(contents)

      for c in bag[0]:
        if c in bag[1]:
          total+=getPriority(c)
          break

  print(total)

if __name__ == '__main__': main()