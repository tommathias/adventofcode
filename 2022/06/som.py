#!/usr/bin/python3
with open('input.txt') as f:
  for line in f:
    #could read and buffer, but take slice
    line = line.strip() #remove \n from end of line
    for i in range(len(line)):
      somLen = 14 #start-of-message marker
      somSlice = slice(i, i+somLen)
      somStr = line[somSlice]
      somSetList = list(set(somStr))
      if len(somSetList) == somLen: #reached end of line
        print(f'[{i}:{i+somLen}] {somStr}')
        break