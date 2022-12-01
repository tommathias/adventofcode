#!/usr/bin/python
import time


start = time.time()
import calories
print(f'calories took { time.time() - start}')

start = time.time()
import podium
print(f'podium took { time.time() - start}')


start = time.time()
import elves
print(f'elves took { time.time() - start}')
