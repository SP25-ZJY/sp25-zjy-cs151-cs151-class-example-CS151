import math

#Prompt for a radius
radius_str = input("Enter the radius of your circle: ")
radius_int = float(radius_str)
print("radius is",type(radius_int))
#Apply the area formula
circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

#Output the results
print ("The circumference is: ", circumference, ", and the area is:", area)
