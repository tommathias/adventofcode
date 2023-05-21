#!/usr/bin/python3

def main():
  with open('test.txt') as f:
    for line in f:
      #do stuff here
      print(line)

  print('Thank you for playing Wing Commander')

if __name__ == '__main__': main()