# Prompt the user for age input
age_str = input("Please enter your age (0-120): ")

# Validate input: ensure it's a digit and within the valid range
while not age_str.isdigit() or int(age_str) < 0 or int(age_str) > 120:
    age_str = input("Invalid input. Please enter a valid age (0-120): ")

# Convert the valid input to an integer
age = int(age_str)

# Print the valid age
print(f"Thank you for entering age: {age}")
