def read_single_data(filename):
    data_file = open(filename, 'r')  # Open for Reading
    data = data_file.read()  # Reads value from file into a string
    data_file.close()  # Shut the door, we’re done
    return data

def write_single_data(filename, balance):
    data_file = open(filename, 'w')  # Open file to Write
    data = str(balance)  # Text files only hold text, a.k.a. strings
    data_file.write(data)  # Write balance to file
    # balance_file.write(27)  # Would also write to file
    data_file.close()  # Close the file because we’re done
    
    
def file_data_to_list(filename):
    # Open the file for reading
    file_data = open(filename, 'r')

    # Read all lines from the file and store them as a list of strings
    values = file_data.readlines()

    # Close the file
    file_data.close()

    # Return the list of lines from the file
    return values


def main():
    # Read the contents of 'grades.txt' into the 'grades' list
    grades = file_data_to_list('grades.txt')

    # Print the number of elements in the 'grades' list
    print(len(grades))

    # Print the first 10 elements of the 'grades' list
    print(grades[:10])


# Call the main function to execute the code
main()