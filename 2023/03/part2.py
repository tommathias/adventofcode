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

  def at(x, y):
    return grid[y][x]
  
  def isInBounds(x,y):
    return x >= 0 and x <= dimensions[0] and y >= 0 and y <= dimensions[1]
  
  def getNumberAt(x,y):
    if not isInBounds(x,y): return None
    if at(x,y).isdigit():
      #walk left to start of number, then walk back to right, then parse
      nFrom = x
      for nx in range(x, -1, -1):
        if at(nx, y).isdigit(): nFrom = nx
        else: break
      stringN = ''
      for nx in range(nFrom, dimensions[0]+1): #walk the width
        if at(nx,y).isdigit(): stringN += at(nx, y)
        else: break
      return int(stringN)
    else: return None
  
  def investigateGearAt(x,y):
    #check for numbers clockwise from NW
    #NW, N, NE  n1, n2, n3
    #W,  *,  E    , * ,  
    #SW, S, SE  s1, s2, s3
    #if found, get whole number
    #dedupe numbers that spans different locations, e.g.
    #...456..
    #....*...
    #.......
    #that is a single number, that spans
    neighbours = []
    #circumstances
    #a.b is the only weird one, we add both
    #otherwise, move from left to right, and only add it if you haven't already
    if y > 0:
      nw = at(x-1, y-1)
      n = at(x, y-1)
      ne = at(x+1, y-1)
      if nw.isdigit() and not n.isdigit() and ne.isdigit():
        #a.b
        neighbours.append(getNumberAt(x-1, y-1))
        neighbours.append(getNumberAt(x+1, y-1))
      elif nw.isdigit(): neighbours.append(getNumberAt(x-1, y-1))
      elif n.isdigit(): neighbours.append(getNumberAt(x, y-1))
      elif ne.isdigit(): neighbours.append(getNumberAt(x+1, y-1))
    
    #e and w
    if at(x-1, y).isdigit(): neighbours.append(getNumberAt(x-1, y))
    if at(x+1, y).isdigit(): neighbours.append(getNumberAt(x+1, y))
    
    if y < dimensions[1]:
      sw = at(x-1, y+1)
      s = at(x, y+1)
      se = at(x+1, y+1)
      if sw.isdigit() and not s.isdigit() and se.isdigit():
        #a.b
        neighbours.append(getNumberAt(x-1, y+1))
        neighbours.append(getNumberAt(x+1, y+1))
      elif sw.isdigit(): neighbours.append(getNumberAt(x-1, y+1))
      elif s.isdigit(): neighbours.append(getNumberAt(x, y+1))
      elif se.isdigit(): neighbours.append(getNumberAt(x+1, y+1))
    
    print(f'gear neighbours: {neighbours}')
    if len(neighbours) == 2:
      print('exactly 2 neighbours!')
      #don't faff with numpy or math, we know we have 2, just multiply them
      product = neighbours[0] * neighbours[1]
      nonlocal sumOfProducts
      sumOfProducts += product

  #start to walk grid
  sumOfProducts = 0

  for y in range(0, dimensions[1]+1):
    print(f'line: {y}')
    for x in range(0, dimensions[0]+2):
      a = at(x,y)
      match a:
        case '*':
          print(f'potential gear at ({x}, {y})')
          investigateGearAt(x,y)
        case _:
          pass
  
  print(sumOfProducts) 
  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
