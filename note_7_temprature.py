print("This program will tell you if a temperature is too hot")
temp = input("What is the temperature?")
temp = float(temp)

# How do we modify so that we can also note if it's too cold?
if temp > 90:
  print("Temperature is too hot")
elif temp < 40:
  print("Temperature is too cold")
else:
  print("Temperature is fine")
