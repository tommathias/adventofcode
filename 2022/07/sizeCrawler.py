#!/usr/bin/python3
import re
verbose = False

# def updateFs(fileSystem, pwdStack):
#   parent = None
#   for dirName in pwdStack:
#     if parent == None:
#       parent = fileSystem['root']
#       continue
#     if not dirName in parent:
#       parent[dirName] = {}
#     parent = parent[dirName]
#   return parent

def aggregateSize(results, pwdStack, fileSize):
  for dirName in pwdStack:
    if dirName not in results:
      results[dirName] = 0
    results[dirName] += int(fileSize)

with open('input.txt') as f:
  fileSystem = {}
  pwdStack = []
  #pwd = {}
  results = { 'root' : 0 }

  for line in f:
    if verbose: print(f'line: {line}')
    if verbose: print(f'pwdStack: {pwdStack}')
    #if verbose: print(f'pwd: {pwd}')
    #for python 3.8, so no match/case
    if line[0] == '$':
      cdMatch = re.match('^\$ cd (.*)$', line) # get cd arg into group
      if cdMatch:
        if verbose: print(f'cd: {cdMatch.group(1)}')
        newDir = cdMatch.group(1)
        if newDir =='..':
          pwdStack.pop()
          newDir = pwdStack[-1]
        else:
          if newDir == '/':
            newDir = 'root'
            pwdStack.append(newDir)
            fileSystem['root'] = {}
          else:
            pwdStack.append(newDir)
            #pwd = updateFs(fileSystem, pwdStack)
      else:
        if verbose: print('ls')
    else:
      # will be an ls output line
      dirMatch = re.match('^dir (.*)$', line)
      if dirMatch:
        #pwd[dirMatch.group(1)] = {}
        continue
      fileMatch = re.match('^(\d.*) (.*)$', line)
      fileSize = fileMatch.group(1)
      fileName = fileMatch.group(2)
      #pwd[fileName] = fileSize
      aggregateSize(results, pwdStack, fileSize)
    if verbose: print('=====')

#if verbose: print(f'fileSystem: {fileSystem}')
print(results)

result = 0
for dirSize in results.values():
  if dirSize <= 100000:
    result += dirSize
print(result)

print('Thank you for playing Wing Commander')
