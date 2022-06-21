#Program objective: Read two digits and print their sum

inputs = input("Enter two digits with a space in between: ")

print("The sum is", int(inputs.split()[0]) + int(inputs.split()[1]))