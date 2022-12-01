floor = 0

#could count ( and ), but simpler to walk chars in line
with open('input.txt') as f:
  for line in f:
    for char in line:
      if char == "(":
        floor+=1
      else:
        if char == ")":
          floor-=1
      #ignore any non () chars

print(floor)