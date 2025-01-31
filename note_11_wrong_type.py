# Goal: To catch if the user inputs the wrong type of value: 
answer = input("Please enter yes or no: ")
answer = answer.lower().strip()

while answer != "yes" and answer != "no":
  print("Sorry, that was not an option") 
  answer = input("Please enter yes or no: ")
  answer = answer.lower().strip()
  
#rest of the program can run
if answer == "yes":
  print("You win a prize!")
else:
  print("You go home empty handed!") 
print("Thanks for playing!")
