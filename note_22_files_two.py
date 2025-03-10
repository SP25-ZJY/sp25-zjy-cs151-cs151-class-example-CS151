import os

def read_filename():
  name = input("Filename to read?")
  while not os.path.isfile(name):
    print("File doesn't exist")
    name = input("Filename to read?")
  return name
  
def read_file_to_list(filename):
  try:
    fd = open(filename,'r') #open for Reading
    values = fd.readlines() #every line of the file is a string in the list
    fd.close() #shut the door, we’re done
    return values
  except:
    print("Error reading file")
    return []

def read_file_to_list_int(filename):
  try:
    fd = open(filename,'r') #open for Reading
    grades = []
    for line in fd:
      line = int(line)
      grades.append(line)
    fd.close() #shut the door, we’re done
    return grades
  except:
    print("Error reading file")
    print(line)
    return []

def write_list(my_list, filename):
  fd = open(filename, "w")
  for item in my_list:
    fd.write(str(item))
    fd.write("\n")
  fd.close()
  
def read_file_to_list_split(filename):
  fd = open(filename,'r') #open for Reading
  grades = []
  for line in fd:
    line = line.split()
    #grades.extend(line)
    for item in line:
      item = int(item)
      grades.append(item)
  fd.close() #shut the door, we’re done
  return grades
  
def main():
  filename = read_filename()
  grades = read_file_to_list_int(filename)
  write_list(grades,"output2.txt")
  # rest of code doesn’t care where it came from, just knows it’s a list
  print(len(grades))
  print(grades)
"""
  average = sum(grades) / len(grades)
  minimum = min(grades)
  maximum = max(grades)

  print(average,minimum,maximum)
  """
main()