#!/usr/bin/python3
verbosity = 1
part = 1
files = ['test.txt', 'input.txt', 'input.txt']

directions = [(0,-1), (1, 0), (0, 1), (-1,0)] #N,E,S,W

class map:
  width: 0
  height: 0
  map: list

  def __init__(self, map: list):
    self.map = map
    self.width = len(map[0])
    self.height = len(map)

class walk:
  walkMap: map
  visited: set
  stepsTaken: int
  stepLimit: int
  highestPoint: tuple
  isFinished: bool

  def __init__(self, map:map, stepLimit:int):
    self.walkMap = map
    self.visited = set()
    self.stepsTaken = 0
    self.stepLimit = stepLimit
    #rather than faff with an offset for ord(l), use a fake starting ord equal to ord('a')-1
    self.highestPoint = (96, 0) #(ord, depth)
    self.isFinished = False

def lineToMap(line:str):
  lineArr = []
  for char in line:
    lineArr.append(char)
  return lineArr

def buildMap():
  mapLines = []
  with open(files[part]) as f:
    for line in f:
      mapLines.append(lineToMap(line.strip()))
  return map(mapLines)

def findStart(map:map):
  for y, line in enumerate(map.map):
    for x, char in enumerate(line):
      if ord(char) == 83: return (x, y)

def heightAt(map: list, coords: tuple):
  return map[coords[1]][coords[0]]

def withinMap(map: list, coords: tuple):
  return coords[0] >= 0 and coords[0] < map.width and coords[1] >= 0 and coords[1] < map.height

def canClimb(place: str, neighbour: str):
  #handle start and end of walk which have different ord(l) values
  if place == 'S' and neighbour == 'a': return True
  if place == 'z' and neighbour == 'E': return True

  return abs(ord(place) - ord(neighbour)) < 2

def getNeighbours(walk: walk, coords: tuple):
  neighbours = []
  for d in directions:
    neighbourCoords = (coords[0] + d[0], coords[1] + d[1])

    if withinMap(walk.walkMap, neighbourCoords) and \
        canClimb(heightAt(walk.walkMap.map, coords), heightAt(walk.walkMap.map, neighbourCoords)) and \
        neighbourCoords not in walk.visited:
      neighbours.append(neighbourCoords)
  return neighbours


def step(stepTo: tuple, walk: walk, stepNow: int): #walk, just a couple of people walking. Oh wait, I'm only one person
    if walk.isFinished: return
    if walk.stepsTaken >= walk.stepLimit: return # prevent infinite walks
    if stepTo in walk.visited: return # prevent loops

    walk.visited.add(stepTo)
    walk.stepsTaken += 1
    height = heightAt(walk.walkMap.map, stepTo)

    #ord(l) for letters: a-z: 97-122, E: 69 nice, S: 83
    # if we hit z we have found the closest, highest point, return current depth
    # if we hit E return the depth of the first step we found the highest point
    if ord(height) > walk.highestPoint[0]:
      walk.highestPoint = (ord(height), stepNow)

    if height == 'E' or height == 'z':
        walk.isFinished = True
        return

    neighbours = getNeighbours(walk, stepTo)

    if verbosity > 0: print(f'current: {stepTo}, height: {height}, neighbours: {neighbours}')

    #DFS, in the order of directions list
    for neighbour in neighbours:
      step(neighbour, walk, stepNow+1)

def walkMap(map: map):
  start = findStart(map)
  theWalk = walk(map, 10_000)
  step(start, theWalk, 1)
  print(theWalk.highestPoint)

def main():
  #create 2d array of map
  map = buildMap()

  #getrecursionlimit() returns 1000
  #walk can recurse to the limit of the map area if it walks every point
  #override the recursion limit to the area of the map
  #I mean, what's the worst I can do? Crash and restart?
  mapArea = map.height * map.width
  import sys
  sys.setrecursionlimit(mapArea)

  if verbosity > 1: print(map)

  #hold on to your butts
  walkMap(map)
  sys.setrecursionlimit(1000)

  #maybe? use Dijkstra's algorithm to find the shortest path

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()