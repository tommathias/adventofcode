#"!/usr/bin/python3
import re

verbose=True
def main():
  total = 0
  with open('input.txt') as f:
    for line in f:
      #match numbers from line
      numberString = re.sub('[a-z]', '',  line) 
      if verbose: print(f'numberString: {numberString}')
      #build string for calibration, final character is newline, so use -2 
      calibrationString=numberString[0]+numberString[-2]
      if verbose: print(f'calibrationString: {calibrationString}')
      total+=int(calibrationString)
      if verbose: print(f'total: {total}')

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()
