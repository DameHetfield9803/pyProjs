salary = float(input("Please enter your salary (before CPF) > "))
cpf = salary * 0.20
cpftotal= cpf + (salary*0.17) # given by employer/organization
print("Your CPF is ", str(cpftotal))
remaining = salary - cpf
chiRemaining = 0
race = input("Please enter your race : ")
if race.capitalize() == "Chinese":
    chiRemaining = float(remaining) -1
    print("Your remaining salary is ",str(chiRemaining)," after deduction from CPF and CDAC \n")
else:    
    print("Your remaining salary is ",str(remaining), " after CPF \n")
