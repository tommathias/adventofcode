#!/usr/bin/python
runningTotal = 0
elves = []

with open('input.txt') as f:
  for line in f:
    if line != "\n":
      runningTotal += int(line)
    else:
      elves.append(runningTotal)
      runningTotal = 0

elves.sort(reverse=True)
print(sum(elves[0:3]))