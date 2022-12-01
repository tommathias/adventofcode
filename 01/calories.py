#!/usr/bin/python
runningTotal = 0
highest = 0

with open('calories.txt') as f:
  for line in f:
    if line != "\n":
      iline = int(line)
      runningTotal += iline
    else:
      if runningTotal > highest:
        highest = runningTotal
      runningTotal = 0

print(highest)
