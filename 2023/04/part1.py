#!/usr/bin/python3
import sys
verbosityLevel=2

def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')
  totalPoints = 0

  with open(srcFile) as f:
    for line in f:
      #read winning numbers
      splitLine = line.split(':')[1].split('|')
      winners = splitLine[0].strip().split(' ')
      numbers = splitLine[1].strip().split(' ')
      if verbosityLevel > 1: print(f'winners:{winners}')
      if verbosityLevel > 1: print(f'numbers:{numbers}')
      #get matches
      matches = 0
      for number in numbers:
        if number == '': continue #ignore empty strings caused by '01' rendered as ' 1'
        if number in winners:
          if verbosityLevel > 1: print(f'{number} is a match')
          matches+=1
      #calculate points: 2^n-1
      if matches == 0: continue
      cardPoints = 2**(matches-1)
      if verbosityLevel > 1: print(f'{matches} matches and {cardPoints} points for this card')
      totalPoints+=cardPoints

  print(totalPoints)
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
