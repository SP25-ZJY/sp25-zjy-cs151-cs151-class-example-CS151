temp = float(input("What is the temperature?"))

comfortLevel = "cold"
if temp > 70:
  if temp > 90:
    comfortLevel = "hot"
  else:
    comfortLevel = "comfortable"
