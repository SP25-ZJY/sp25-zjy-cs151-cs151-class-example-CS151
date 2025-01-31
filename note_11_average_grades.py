# Goal: Average together 3 test grades
#Initialize variables
sum = 0
count = 0
total_grades=int(input("How many grades?"))

#read in and sum the 3 grades
while count < total_grades:
  #sum += float(input("Please enter grade: "))
  count = count - 1
  print(count)

#find average and output it 
average = sum / total_grades
print("The average is",average)



