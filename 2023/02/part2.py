#!/usr/bin/python3
import sys
verbosityLevel=1


def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')
  sumOfPowers = 0

  with open(srcFile) as f:
    for line in f:
      #trim newline as it always appears on a string of colours that causes key parsing issues
      game = line.replace('\n','').split(':')
      gameNumber = game[0].split(' ')[-1]
      if verbosityLevel > 0: print(f'gameNumber: {gameNumber}')  
      rounds = game[1].split(';')
      gameBalls = {
          "red": 0,
          "green": 0,
          "blue": 0
          }
      
      #round is reserved word
      for thisRound in rounds:
        if verbosityLevel > 1: print('Start Round')

        showings = thisRound.split(',')
        for showing in showings:
          detail = showing.split(' ')
          
          #showing sections will always have a leading space giving e.g. detail: ['', '3'. 'blue']
          colour = detail[2]
          n = int(detail[1])
          if (gameBalls[colour] < n): gameBalls[colour] = n 
        
        if verbosityLevel > 1: print(gameBalls)
      if verbosityLevel > 0: print(gameBalls)
      power = gameBalls['red'] * gameBalls['green'] * gameBalls['blue']
      if verbosityLevel > 0: print(f'power: {power}')
      sumOfPowers += power
  print(f'sumOfPowers: {sumOfPowers}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
