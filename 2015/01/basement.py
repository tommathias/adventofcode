floor = 0
position = 0

#could count ( and ), but simpler to walk chars in line
with open('input.txt') as f:
  for line in f:
    #print(len(line))
    for char in line:
      position+=1 #1 based index for solution, increment here
      if char == "(":
        floor+=1
      else:
        if char == ")":
          floor-=1
      #ignore any non () chars
      if floor == -1:
      #no need to break outer loop, input is a single line
        break

print(position)
