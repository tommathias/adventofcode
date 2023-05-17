#!/usr/bin/python3.10
import re
logLevel = 0

def aggregateSize(results, pwdStack, fileSize):
  #qualify names in results to prevent collisions
  path = ''
  for dirName in pwdStack:
    path = '/'.join([path, dirName])
    if path not in results:
      results[path] = 0
    results[path] += int(fileSize)

with open('input.txt') as f:
  pwdStack = []
  results = { }

  for line in f:
    if logLevel > 0: print(f'line: {line}')
    if logLevel > 0: print(f'pwdStack: {pwdStack}')
    match line.split(): # can match on structured data not just literals
      case '$', 'cd', '/':
        if logLevel > 1: print('cd /')
        pwdStack = ['root']
      case '$', 'cd', '..':
        if logLevel > 1: print('cd ..')
        pwdStack.pop()
      case '$', 'cd', dir:
        if logLevel > 1: print(f'cd {dir}')
        pwdStack.append(dir)
      case '$', 'ls':
        if logLevel > 1: print('ls')
      case 'dir', dir:
        if logLevel > 1: print(f'dir: {dir}')
      case fileSize, fileName:
        if logLevel > 1: print(f'file: {fileName, fileSize}')
        aggregateSize(results, pwdStack, fileSize)
      case _:
        raise('no line match')
    if logLevel > 0: print(f'pwdStack: {pwdStack}')
    if logLevel > 0: print('=====')

print(results)

# part 1
result = 0
for dirSize in results.values():
  if dirSize <= 100000:
    result += dirSize
print(result)

# part 2

total = 70000000
needed = 30000000

used = results['/root']
unused = total - used
toDelete = needed - unused

#get dirs that match, pick smallest
candidates = []
for size in results.values():
  if size > toDelete:
    candidates.append(size)
candidates.sort()
print(candidates[0])


print('Thank you for playing Wing Commander')
