#!/usr/bin/python3
import sys
verbosityLevel=2

def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')
  totalPoints = 0
  cards=[0]
  totalCards = 0

  def addCards(i, n):
    nonlocal cards
    if i > len(cards)-1: cards.append(0)
    cards[i] += n

  with open(srcFile) as f:
    for i, line in enumerate(f):
      #add self to final cards
      addCards(i, 1)
      print(cards)
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
      if matches > 0:
        cardPoints = 2**(matches-1)
        if verbosityLevel > 1: print(f'{matches} matches and {cardPoints} points for this card')
        totalPoints+=cardPoints
      #insert a card for each win
      for j in range(1, matches+1):
        addCards(i+j, cards[i])
      totalCards+=cards[i]
      print(totalCards)

  print(f'totalPoints: {totalPoints}, totalCards: {totalCards}')
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
