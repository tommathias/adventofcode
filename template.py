#!/usr/bin/python3
import sys
verbosityLevel=1

def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')

  with open(srcFile) as f:
    for line in f:
      #do stuff here
      print(line)

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
