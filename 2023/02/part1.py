#!/usr/bin/python3
import sys
verbosityLevel=1

def isGamePossible(bagMax, ballsSeen):
  for colour in bagMax:
    if (ballsSeen[colour] > bagMax[colour]): return False
  return True

def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')
  
  possibleGameSum = 0
  bagMax={
          "red": 12,
          "green": 13,
          "blue": 14
          }

  with open(srcFile) as f:
    for line in f:
      #trim newline as it always appears on a string of colours that causes key parsing issues
      game = line.replace('\n','').split(':')
      gameNumber = game[0].split(' ')[-1]
      if verbosityLevel > 0: print(f'gameNumber: {gameNumber}')  
      ballsSeen={
              "red": 0,
              "green": 0,
              "blue": 0
              }

      rounds = game[1].split(';')
      #round is reserved word
      for thisRound in rounds:
        showings = thisRound.split(',')
        for showing in showings:
          detail = showing.split(' ')
          if verbosityLevel > 1: print(f'ballsSeen: {ballsSeen}, game: {game}, thisRound: {thisRound}, showing: {showing}, detail: {detail}')
          #showing sections will always have a leading space giving e.g. detail: ['', '3'. 'blue']
          ballsSeen[detail[2]] += int(detail[1])
      if verbosityLevel > 0: print(f'ballsSeen: {ballsSeen}')  
      if isGamePossible(bagMax, ballsSeen): possibleGameSum += int(gameNumber)
      if verbosityLevel > 0: print(f'possibleGameSum: {possibleGameSum}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
