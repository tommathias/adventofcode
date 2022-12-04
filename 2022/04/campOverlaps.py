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
    first = []
    second = []
    if s2 >= s1:
      first = [s1, e1]
      second = [s2, e2]
    else:
      second = [s1, e1]
      first = [s2, e2]

    print(f'first:{first}, second:{second}')

    if first[1] >= second[0]:
      print(f'hit:{line}')
      count+=1
      continue

    print(f'miss:{line}')


print(count)