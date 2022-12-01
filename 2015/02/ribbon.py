#!/usr/bin/python3
total = 0
with open('input.txt') as parcels:
  for parcel in parcels:
    #"orient" parcels in asc order, helps with slack calculations
    #cast to int before sorting, otherwise it will sort by text e.g. 20 being larger than 100
    dimensions = sorted(map(int, parcel.split('x')))
    l=int(dimensions[0])
    w=int(dimensions[1])
    h=int(dimensions[2])

    #ribbon = smallest perimeter = 2*l+w
    #bow = cubic volume = l*w*h
    sum = 2*(l+w) + (l*w*h)
    #print(f'parcel: {parcel} needs {ribbon}')
    total += sum

print(total)