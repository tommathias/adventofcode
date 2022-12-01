#!/usr/bin/python
runningTotal = 0
gold = 0
silver = 0
bronze = 0
# avoid list approach as sorting is expensive

with open('input.txt') as f:
  for line in f:
    if line != "\n":
      runningTotal += int(line)
    else:
      #unrolled evaluation for podium
      if runningTotal > gold:
        bronze = silver
        silver = gold
        gold = runningTotal
      else:
        if runningTotal > silver:
          bronze = silver
          silver = runningTotal
        else:
          if runningTotal > bronze:
            bronze = runningTotal

      runningTotal = 0


print(gold + silver + bronze)
