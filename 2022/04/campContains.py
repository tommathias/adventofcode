#!/usr/bin/python3
count = 0

with open('input.txt') as f:
  for line in f:
    #print(line)
    #range, start, end and length
    r = line.split(',')
    r1 = r[0].split('-')
    s1 = int(r1[0])
    e1 = int(r1[1])
    l1 = e1-s1

    r2 = r[1].split('-')
    s2 = int(r2[0])
    e2 = int(r2[1])
    l2 = e2-s2

    #check fully contains
    if l1 == l2 and s1 == s2:
      #print(line)
      count+=1
      continue

    #start, end, length
    large = []
    small = []
    if l1 > l2:
      large = [s1, e1, l1]
      small = [s2, e2, l2]
    else:
      small = [s1, e1, l1]
      large = [s2, e2, l2]

    #small.start >= large.start &&
    #small.end <= large.end &&
    #large.start + small.length >= large.end
    if small[0] >= large[0] and small[1] <= large[1] and large[0]+small[2] <= large[1]:
      #print(line)
      count+=1

print(count)