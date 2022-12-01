#!/usr/bin/python
runningTotal = 0
elves = []

with open('calories.txt') as f:
  for line in f:
    if line != "\n":
      iline = int(line)
      runningTotal += iline
    else:
      elves.append(runningTotal)
      runningTotal = 0

elves.sort(reverse=True)
print(sum(elves[0:3]))