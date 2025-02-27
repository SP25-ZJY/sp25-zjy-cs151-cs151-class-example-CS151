def isfloat(value):
    temp = value.replace(".", "", 1)  # Replace only the first period
    return temp.isdigit() or (temp.startswith("-") and temp[1:].isdigit())


def input_float():
    value = input("Please enter the value: ")
    while not isfloat(value):
        print("You must enter a valid number with decimal points.")
        value = input("Please enter a new value: ")
    return float(value)


def main():
    print("What is the cost?")  # In case you need a description
    cost = input_float()  # Call the error-check function
    print(f'Cost = {cost:.2f}')  # Display the cost with 2 decimal places

main()