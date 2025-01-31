value = input("Please input a grade (integer)")
while not value.isdigit():
  print("input must be an integer")
  value = input("Please input a grade (integer)")
value = int(value)
print("got to end")