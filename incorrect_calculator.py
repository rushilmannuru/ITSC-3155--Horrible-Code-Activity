def calculate_1():
    num1=float(input("Enter the first number"))
    num2=float(input("Enter the second number"))
    choice=input("Enter 1 for addition and 2 for subtraction")
    if choice=="1":
        print(num1+num2)
    elif choice=="2":
        print(num1-num2)
    else:
        print("You didn't pick 1 or 2")

def calculate_2():
    num1=float(input("Enter the first number"))
    num2=float(input("Enter the second number"))
    choice=input("Enter 1 for multiplication and 2 for division")
    if choice=="1":
        print(num1*num2)
    elif choice=="2":
        print(num1*num2)
    else:
        print("You didn't pick 1 or 2")

def pick_job():
    print("Pick calculation")
    choice=input("Enter 1 for + or - and 2 for * or /")
    if choice=="1":
        calculate_1()
    elif choice=="2":
        calculate_2()
    else:
        print("You didn't pick 1 or 2")


pick_job()
