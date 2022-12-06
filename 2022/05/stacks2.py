#!/usr/bin/python3
fileName = 'input.txt'

def buildStacksFrom(fileName):
  #input file in format stack contents/stack definition/\n/moves
  #read lines until stack definition i.e. lines[1] = 1
  stacks = []
  with open(fileName) as f:
    for line in f:
      if (line[1] != '1'): continue
      #format is : 1   2  ..  n  \n so count of stacks in len/4
      nStacks = int(len(line)/4)
      #print(f'n:{nStacks}')
      for i in range(nStacks):
        stacks.append([])
      return stacks

def populateFrom(stacks, fileName):
  #reading from file pushes to stack from the top
  #read lines in reverse order then invert the stacks
  with open(fileName) as f:
    for line in f:
      if (line[1] == '1'): #reached stack definition line
        for i in range(len(stacks)):
          stacks[i].reverse()
        return stacks 

      #print(line)
      nStacks = len(stacks)
      for i in range(nStacks):
        #format is : 1   2  ..  n  \n so count of stacks in len/4
        stackSlice = slice(i*4, (i*4)+3)
        square = line[stackSlice]
        if square == '   ': continue #empty square
        #print(f'square{i}: {square}')
        stacks[i].append(square[1])

stacks = buildStacksFrom(fileName)
stacks = populateFrom(stacks, fileName)

with open(fileName) as f:
  for line in f:
    if (line[0] != 'm'): continue #not a move line
    move = line.split(' ')
    count = int(move[1])
    srci = int(move[3])-1
    desti = int(move[5])-1
    #print(f'moving {count} from {src} to {dest}')
    #print(stacks)
    temp = []
    for i in range(count):
      #could take slice in order, but simulate by popping into temp and pushing out
      temp.append(stacks[srci].pop())
    for i in range(count):
      stacks[desti].append(temp.pop())
    #print(stacks)


result = ''
for stack in stacks:
  result+=stack.pop()
print(result)