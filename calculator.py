def calculator():
    i = input("Please enter an operator to trigger for math operations > ")
    num1 = int(input("Please enter the first number > "))
    num2 = int(input("Please enter the second number > "))
    if i == "+":
        print(num1 + num2)
    if i == "-":
        print(num1 - num2)  
    if i == "*":
        print(num1 * num2)
    if i == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1/num2)
    if i == "%":
        print(num1 % num2)
    if i == "**":
        print(num1**num2)
    if i == "//":
        print(num1//num2)

def tempConverter():
    firstu = str(input("Please enter the the first measuring unit to convert from one to another (C/F/K) > "))
    secondu = str(input("Please enter the the second measuring unit to convert from one to another (C/F/K) > "))
    if firstu.capitalize() == "C" and secondu.capitalize() == "F":
        print("You have chosen to convert from Celsius to Fahrenheit")
        c2f= input("Please enter the temperature to convert from C to F > ")
        if c2f.isnumeric():
            c2f = int(c2f)
            print("The temperature in Fahrenheit is", (c2f * 9/5) + 32)
    elif firstu.capitalize() == "F" and secondu.capitalize() == "C":
        print("You have chosen to convert from Fahrenheit to Celsius")
        f2c = input("Please enter the temperature to convert from F to C > ")
        if f2c.isnumeric():
            f2c = int(f2c)
            print("The temperature in Celsius is", (f2c - 32) * 5/9)
    elif firstu.capitalize() == "K" and secondu.capitalize() == "C":
        print("You have chosen to convert from Kelvin to Celsius")
        k2c= input("Please enter the temperature to convert from K to C > ")
        if k2c.isnumeric():
            k2c = int(k2c)
            print("The temperature in Celsius is", k2c - 273.15)
    elif firstu.capitalize() == "C" and secondu.capitalize() == "K":
        print("You have chosen to convert from Celsius to Kelvin")
        c2k= input("Please enter the temperature to convert from C to K > ")
        if c2k.isnumeric():
            c2k = int(c2k)
            print("The temperature in Kelvin is", c2k + 273.15)
    else:
        print("Please enter a valid unit of measurement (C/F/K)")
        
def bmiCalculator():
    w = float(input("Please enter your weight in kilograms > "))
    h = float(input("Please enter your height in meters > "))
    if w == 0:
        print("Please enter a valid weight as that is not physically possible")
    elif h == 0:
        print("Please enter a valid height as that is not physically possible")
    else:
        print("Your BMI is ", w/(h**2))

def exit():
    print("Thank you for using the program")
    print("Exiting...")
    

def main():
    print("**********************")
    print("Press 1 to use calculator \n")
    print("Press 2 to use BMI calculator \n")
    print("Press 3 to use temperature converter \n")
    print("Press 4 to quit")
    print("**********************")
    choice = int(input("Please enter your choice > "))
    if choice == 1:
        calculator()
    elif choice == 2:
        bmiCalculator()
    elif choice == 3:
        tempConverter()
    elif choice == 4:
        exit()
    else:
        print("Please enter a valid choice")
