#!/usr/bin/python3
import sys
verbosityLevel=2

def isShowingPossible(bagMax, ballsSeen):
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
      rounds = game[1].split(';')
      if verbosityLevel > 0: print('Start Game')
      gameIsPossible = True

      #round is reserved word
      for thisRound in rounds:
        if not gameIsPossible: break #for round
        if verbosityLevel > 0: print('Start Round')
        deez = {
          "red": 0,
          "green": 0,
          "blue": 0
          }

        showings = thisRound.split(',')
        for showing in showings:
          detail = showing.split(' ')
          #if verbosityLevel > 1: print(f'showing: {showing}, detail: {detail}')
          
          #showing sections will always have a leading space giving e.g. detail: ['', '3'. 'blue']
          deez[detail[2]] += int(detail[1])
        
        print(deez)
        if not isShowingPossible(bagMax, deez):
          if verbosityLevel > 0: print('impossible')
          gameIsPossible = False
          break #for showing

      if gameIsPossible: possibleGameSum += int(gameNumber)

      if verbosityLevel > 0: print(f'possibleGameSum: {possibleGameSum}')
  print(possibleGameSum)
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
