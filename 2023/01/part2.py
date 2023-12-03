#"!/usr/bin/python3
import sys, re

verbosityLevel = -1
nWords=[
    ['one', '1'],
    ['two', '2'],
    ['three', '3'],
    ['four', '4'],
    ['five', '5'],
    ['six', '6'],
    ['seven', '7'],
    ['eight', '8'],
    ['nine', '9']
    ]

def main():
  srcFile = 'test2.txt'
  if (len(sys.argv) > 1): srcFile = sys.argv[1]
  if verbosityLevel > 0: print(f'srcFile: {srcFile}')

  total = 0
  #original approach of re.sub doesn't work for finding the first text number, use re.match
  with open(srcFile) as f:
    for line in f:
      if verbosityLevel >0: print('----------')
      if verbosityLevel >0: print(f'line: {line}')
      #match numbers from line, use lookahead to not consume the match from the string
      r = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
      if verbosityLevel > 1: print(f'r: {r}')
      calibrationString=r[0]+r[-1]
      if verbosityLevel > 1: print(f'calibrationString: {calibrationString}')
      for nWord in nWords: calibrationString = calibrationString.replace(nWord[0], nWord[1])
      if verbosityLevel > 0: print(f'calibrationString: {calibrationString}')
      total+=int(calibrationString)
      if verbosityLevel > 0: print(f'total: {total}')
      if verbosityLevel < 0: print(total)

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
