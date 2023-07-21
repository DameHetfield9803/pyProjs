import math #importing math module

'''def isinteger():
    try:
        int(input("Enter a number > "))
        return input
    except ValueError:
        return "Invalid input. Please enter an integer."

def isPrime():
    input = int(input("Enter a number > "))
    if input.isinteger() == False:
        ValueError("Please enter an integer.")
    else:
        if input > 0 and input > 1 and math.sqrt(input) % 1 != 0:
            print("It is a prime number. \n")
        elif math.sqrt(input) % 1 == 0:
            print("It is not a prime number. \n")

isPrime()'''

import math  # importing math module

def get_integer_input():
    try:
        return int(input("Enter a number > "))
    except ValueError:
        raise ValueError("Invalid input. Please enter an integer.")

def is_prime(num):
    if num < 2:
        return False

    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False

    return True

def isPrime():
    try:
        input_num = get_integer_input()
        if is_prime(input_num):
            print("It is a prime number.")
        else:
            print("It is not a prime number.")
    except ValueError as e:
        print(str(e))

isPrime()