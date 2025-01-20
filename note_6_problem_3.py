print("This program will calculate x*y/b")
# Get input
x = float(input("What is x?"))
y = float(input("What is y?"))
b = float(input("What is b?"))
# Make decision
if b != 0:  # COLON
    result = x * y / b
    print("Result:", result)

else:
    print("Thou shalt not divide by zero")
