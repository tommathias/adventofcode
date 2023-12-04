#!/usr/bin/python3
import sys
verbosityLevel=1

def main():
  srcFile = 'test.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')
  

  dimensions = [0,0]
  grid = []
  with open(srcFile) as f:
    for i, line in enumerate(f):
      grid.append(line)
      dimensions[0] = len(line.strip()) - 1 #for 0-based co-ords
      dimensions[1] = i

  print(dimensions)
  print(grid)

  sumOfPartNos = 0

  def at(x, y):
    return grid[y][x]
  
  def isSymbol(x,y):
    #if oob return false
    if x < 0 or x > dimensions[0] or y < 0 or y > dimensions[1]:
      if verbosityLevel > 1: print(f'({x},{y}) is OOB')
      return False
    if verbosityLevel > 1: print(f'({x},{y}) is {at(x,y)}')
    return at(x,y) not in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']
    
    
     
  def hasAdjacentSymbol(nFrom, nTo):
    # check for symbol in range:
    #...*******...
    #...*ddddd*...
    #...*******...
    
    targets = []

    #line above
    y = nFrom[1]-1
    for x in range(nFrom[0]-1, nTo[0]+2):
      targets.append((x,y))

    #the line
    targets.append((nFrom[0]-1, nFrom[1]))
    targets.append((nTo[0]+1, nFrom[1]))

    #line below
    y = nFrom[1]+1
    for x in range(nFrom[0]-1, nTo[0]+2):
      targets.append((x,y))
  
    for target in targets:
      #print(f'{isSymbol(target[0], target[1])} at ({target[0]},{target[1]})')
      if isSymbol(target[0], target[1]): return True
    return False


  def finishNumberAt(x,y):
    nonlocal amInN
    nonlocal n
    nonlocal nFrom
    nonlocal nTo
    nonlocal sumOfPartNos

    nTo = (x,y)
    print(f'n: {n}, nFrom: {nFrom}, nTo: {nTo}')
    if hasAdjacentSymbol(nFrom, nTo):
      print(n)
      sumOfPartNos += int(n)

    #reset number
    nTo = (0,0)
    n = ''
    amInN = False

  #start to walk grid
  amInN = False
  n = ''
  nFrom = (0,0)
  nTo = (0,0)

  for y in range(0, dimensions[1]+1):
    print(f'line: {y}')
    for x in range(0, dimensions[0]+2):
      a = at(x,y)
      match a:
        case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
          if not (amInN): nFrom = (x,y)
          amInN = True
          n += a
        case '\n' | '.' | _:
          if amInN: finishNumberAt(x-1,y) #-1 to y, co-ord, it finished on the previous 
 
  print(sumOfPartNos)     
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
