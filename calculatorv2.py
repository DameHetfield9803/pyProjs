# Define the calculator function
def calculator():
    # Get the operator from the user
    i = input("Please enter an operator to trigger for math operations > ")
    # Get the first number from the user
    num1 = int(input("Please enter the first number > "))
    # Get the second number from the user
    num2 = int(input("Please enter the second number > "))
    # Use a dictionary to map the operator to the corresponding operation
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Cannot divide by zero",
        "%": num1 % num2,
        "**": num1 ** num2,
        "//": num1 // num2
    }
    # Check if the operator is in the dictionary
    if i in operations:
        # Print the result of the operation
        print(operations[i])
    else:
        # Print an error message if the operator is not in the dictionary
        print("Invalid operator")

# Define the tempConverter function
def tempConverter():
    # Get the first measuring unit from the user
    firstu = input("Please enter the the first measuring unit to convert from one to another (C/F/K) > ").capitalize()
    # Get the second measuring unit from the user
    secondu = input("Please enter the the second measuring unit to convert from one to another (C/F/K) > ").capitalize()
    # Use a dictionary to map the measuring units to the corresponding conversion functions
    conversions = {
        "C->F": lambda x: (x * 9/5) + 32,
        "F->C": lambda x: (x - 32) * 5/9,
        "K->C": lambda x: x - 273.15,
        "C->K": lambda x: x + 273.15
    }
    # Check if the conversion function is in the dictionary
    if firstu + "->" + secondu in conversions:
        # Get the temperature from the user
        temp = input(f"Please enter the temperature to convert from {firstu} to {secondu} > ")
        # Check if the temperature is numeric
        if temp.isnumeric():
            # Convert the temperature to a float
            temp = float(temp)
            # Get the conversion function from the dictionary
            conversion = conversions[firstu + "->" + secondu]
            # Print the result of the conversion
            print(f"The temperature in {secondu} is {conversion(temp)}")
        else:
            # Print an error message if the temperature is not numeric
            print("Invalid temperature")
    else:
        # Print an error message if the conversion function is not in the dictionary
        print("Invalid units of measurement")

# Define the bmiCalculator function
def bmiCalculator():
    # Get the weight from the user
    w = float(input("Please enter your weight in kilograms > "))
    # Get the height from the user
    h = float(input("Please enter your height in meters > "))
    # Check if the weight and height are valid
    if w > 0 and h > 0:
        # Calculate the BMI
        bmi = w / (h ** 2)
        # Print the BMI
        print(f"Your BMI is {bmi}")
    else:
        # Print an error message if the weight or height is not valid
        print("Invalid weight or height")

# Define the exit function
def exit_program():
    # Print a message to thank the user for using the program
    print("Thank you for using the program")
    # Print a message to indicate that the program is exiting
    print("Exiting...")
    # Print a message to indicate that the program has exited
    print("Exited")

# Define the main function
def main():
    # Print the menu
    print("**********************")
    print("Press 1 to use calculator")
    print("Press 2 to use BMI calculator")
    print("Press 3 to use temperature converter")
    print("Press 4 to quit")
    print("**********************")
    # Get the user's choice
    choice = input("Please enter your choice > ")
    # Loop until the user chooses to quit
    while choice != "4":
        # Check the user's choice
        if choice == "1":
            # Call the calculator function
            calculator()
        elif choice == "2":
            # Call the bmiCalculator function
            bmiCalculator()
        elif choice == "3":
            # Call the tempConverter function
            tempConverter()
        else:
            # Print an error message if the choice is not valid
            print("Invalid choice")
        # Print a separator
        print("**********************")
        # Print the menu again
        print("Press 1 to use calculator")
        print("Press 2 to use BMI calculator")
        print("Press 3 to use temperature converter")
        print("Press 4 to quit")
        print("**********************")
        # Get the user's choice again
        choice = input("Please enter your choice > ")
    # Call the exit function
    exit_program()
# Call the main function
main()
