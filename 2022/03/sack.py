#!/usr/bin/python3
compartmentN = 2
total = 0

def getPriority(char):
  if not char.isalpha():
    raise('Can only prioritise letters')

  cOrd = ord(char)
  if(cOrd > 96): #lower
    return cOrd-96
  if(cOrd > 64): #upper
    return cOrd-38
  raise('You werent supposed to be able to get here you know')

lineCount = 0
lines = []
groupSize = 3
with open('input.txt') as f:
  for line in f:
    line = line.strip() #remove \n
    lines.append(line)
    lineCount = len(lines)
    if lineCount > groupSize:
      raise('groups desynced')

    if lineCount < groupSize:
      continue

    #now have group of lines
    print(lines)
    #could recurse to depth of groupSize, but depth known as 3
    found = ''
    for c in lines[0]:
      if c in lines[1] and c in lines[2]:
        found = c
        break
    
    if found == '':
      for c in lines[1]:
        if c in lines[2]:
          found = c
          break
    print(f'found: {c}')
    total+=getPriority(c)

    lines = []

print(total)