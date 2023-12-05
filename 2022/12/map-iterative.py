#!/usr/bin/python3
import map
verbosity = 1
#todo figure out scope of part 
part = 0 # test = 0, part 1 = 1, part 2 = 2
files = ['test.txt', 'input.txt', 'input.txt']

directions = [(0,-1), (1, 0), (0, 1), (-1,0)] #N,E,S,W

def walkMap(walkMap: map.map):
  start = map.findStart(walkMap)
  stepLimit = 40
  theWalk = map.walk(walkMap, stepLimit)
  stepTo = start

  while theWalk.stepsTaken < stepLimit:
    if stepTo in theWalk.visited: yield # prevent loops

    theWalk.visited.add(stepTo)
    theWalk.stepsTaken += 1
    height = map.heightAt(walk.walkMap.map, stepTo)

    #ord(l) for letters: a-z: 97-122, E: 69 nice, S: 83
    if height == 'E':
        walk.isFinished = True
        return

    neighbours = map.getNeighbours(walk, stepTo)

    if verbosity > 0: print(f'current: {stepTo}, height: {height}, neighbours: {neighbours}')

    #DFS, in the order of directions list
    for neighbour in neighbours:
      step(neighbour, walk, stepNow+1)


  print(f'Highest point: {chr(theWalk.highestPoint[0])}, found after {theWalk.highestPoint[1]} steps')
  print('should be lower than 509')

def main():
  #create 2d array of walkMap
  theMap = map.buildMapFor(part)
  if verbosity > 1: print(theMap)

  #hold on to your butts
  walkMap(theMap)

  #maybe? use Dijkstra's algorithm to find the shortest path

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
