#!/usr/bin/python3
with open('input.txt') as f:
  for line in f:
    #could read and buffer, but take slice
    line = line.strip() #remove \n from end of line
    for i in range(len(line)):
      sopLen = 4 #start-of-packet marker
      sopSlice = slice(i, i+sopLen)
      sopStr = line[sopSlice]
      sopSetList = list(set(sopStr))
      if len(sopSetList) == 4: #reached end of line
        print(f'[{i}:{i+sopLen}] {sopStr}')
        break