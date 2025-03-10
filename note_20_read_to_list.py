def isfloat(value):
    temp = value.replace(".", "", 1)  # Replace only the first period
    return temp.isdigit() or (temp.startswith("-") and temp[1:].isdigit())


def input_float(prompt):
    value = input(prompt)
    while not isfloat(value):
        print("You must enter a valid number with decimal points.")
        value = input(prompt)
    return float(value)

def read_grades_to_list():
    my_list = []
    SENTINEL = -100

    value = input_float('Please enter a grade (-100 to end): ')

    while value != SENTINEL:
        my_list.append(value)
        value = input_float('Please enter a grade (-100 to end): ')

    return my_list


def main():
    grades = read_grades_to_list()

    if len(grades) > 0:
        average = sum(grades) / len(grades)
        print("The average grade:", average)
    else:
        print("No valid grades entered.")


main()