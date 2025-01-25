"""
You have the value of the area of a square.
Output the length of the side of the square. 
However, if the value of the area is not a valid value, 
do not do the calculation and output an error message.
"""
import math

area = float(input("Please enter the area:"))

# add code here
if area > 0:
  result = math.sqrt(area)
  print(result)
else:
  print("invalid area")