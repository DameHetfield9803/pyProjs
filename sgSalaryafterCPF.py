salary = float(input("Please enter your salary (before CPF) > "))
cpf = salary * 0.17
print("Your CPF is ", str(cpf))
remaining = salary - cpf
chiRemaining = 0
race = input("Please enter your race : ")
if race.capitalize() == "Chinese":
    chiRemaining = float(remaining) -1
    print("Your remaining salary is ",str(chiRemaining)," after deduction from CPF and CDAC \n")
else:    
    print("Your remaining salary is ",str(remaining), " after CPF \n")