#!/usr/bin/python
runningTotal = 0
highest = 0

with open('input.txt') as f:
  for line in f:
    if line != "\n":
      runningTotal += int(line)
    else:
      if runningTotal > highest:
        highest = runningTotal
      runningTotal = 0

print(highest)
