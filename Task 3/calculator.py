#Calculator with Simple arithmetic Operations

#Function for Addition
def addition():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    print(f"{a+b} is the sum of the given numbers")

#Function for subtraction
def subtraction():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    print(f"{a-b} is the difference of the given numbers")

#Function for Multiplication
def multiply():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    print(f"{a*b} is the product of the given numbers")

#Function for division
def division():
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    if b==0:
        print("Invalid Input")       
    print(f"{a/b} is the quotient of the given numbers")

#Asking user for Input
opt=input("Write add to perform addition\nWrite sub to perform subtraction\nWrite mul to perform mulitplication\nWrite div to perfrom division ")

#Calling a function with reference to the user asked operations
if opt.lower()=="add":
    addition()


elif opt.lower()=="sub":
    subtraction()


elif opt.lower()=="mul":
    multiply()


elif opt.lower()=="div":
    division()
    
else:
    print("Invalid Option")

