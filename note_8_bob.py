print ("This program will determine if both students are taking 15 credits")
#read in values
bob_credits = int(input("How many credits does Bob have?"))

mary_credits = int(input("How many credits does Mary have?"))

if bob_credits >= 15 and mary_credits >= 15:
  print("yes")
else:
  print("no")
#output yes if both credits are at least 15, output no otherwise
"""
if bob_credits >= 15:
  if mary_credits >= 15:
    print("Yes")
  else:
    print("No")
else:
  print("No")
"""

