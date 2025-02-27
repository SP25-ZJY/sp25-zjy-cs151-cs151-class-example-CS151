def read_valid_int():
    value = input("Please enter an integer: ")
    while not value.isdigit():
        value = input("Please enter an integer: ")
    return int(value)

def average_grades(total_grades):
    total = 0
    count = 0

    print("Please enter each grade.")
    while count < total_grades:
        print()
        number = read_valid_int()
        total += number
        count += 1

    average = total / total_grades
    return average

def main():
    print("How many grades?")
    num_grades = read_valid_int()
    avg = average_grades(num_grades)
    print("The average grade is", avg)

main()