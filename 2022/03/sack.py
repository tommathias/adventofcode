#!/usr/bin/python3
import ruck

def main():
  total = 0

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
      total+=ruck.getPriority(c)

      lines = []

  print(total)

if __name__ == '__main__': main()