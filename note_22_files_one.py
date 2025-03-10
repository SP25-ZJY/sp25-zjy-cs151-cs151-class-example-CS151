def read_file_to_list(filename):

  fd = open(filename,'r') #open for Reading

  values = fd.readlines() #every line of the file is a string in the list

  fd.close() #shut the door, we’re done

  return values

def read_file(filename):

    data_file = open(filename, 'r')  # open for Reading

    data = data_file.read()  # reads value from file into a string

    data_file.close()  # shut the door, we’re done

    return data


# Writing a single value
def write_data(filename, balance):

  data_file = open(filename, 'w')  # Open file to Write

  data = str(balance)  # Text files only hold text, a.k.a. strings

  data_file.write(data)  # Write balance to file

  data_file.close()  # Close the file because we’re done

def main():
  grades = read_file_to_list("grades.txt")
  
  # rest of code doesn’t care where it came from, just knows it’s a list
  print(len(grades))
  print(grades[:10])

main()