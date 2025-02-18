def num_input():
    value = input("Please enter an integer: ")
    while not value.isdigit():
        value = input("Please enter an integer: ")
    return int(value)

def average_grades(total_grades):
    total = 0
    count = 0

    print("Please enter each grade.")
    while count < total_grades:
        number = num_input()
        total += number
        count += 1

    average = total / total_grades
    return average

def main():
    print("How many grades?")
    num_grades = num_input()
    avg = average_grades(num_grades)
    print("The average grade is", avg)

main()