#For the sake of the example, let’s assume all grades are integers
#Set up the code
count = 0
sum = 0
SENTINEL = -999	   # some value that isn’t valid for the problem

#Priming read
score_str = input("Give a test score (-999 to end): ")
score = int(score_str)

#continue reading in scores until the user says to stop
while score != SENTINEL:
  sum = sum +score
  count = count+1
  # update read
  score_str = input("Give a test score (-999	 to end): ")
  score = int (score_str)

print(sum)
average = 0
if count !=0:
  average = sum/count
print(average)