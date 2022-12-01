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

    #surface area = 2*l*w + 2*w*h + 2*h*l
    #slack = area of smallest side = l*w
    area = (3*l*w) + (2*w*h) + (2*h*l)
    #print(f'parcel: {parcel} needs {area}')
    total += area

print(total)