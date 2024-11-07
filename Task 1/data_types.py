#Variables of Each Data types
a= int
b= float
c= str
d= bool
#Performing Operations in "INT"  Data type
x=int(input("Enter first number "))
y=int(input("Enter second number "))
print(f"{x+y} is the sum of the numbers")
print(f"{x-y} is the difference of the numbers")
print(f"{x*y}product of the numbers")
print(f"{x/y} is the quotient of the numbers")
#performing operations in "Float" Data type
p=float(input("Enter first number "))
k=float(input("Enter second number "))
print(f"{p+k} is the sum of the numbers")
print(f"{p-k} is the difference of the numbers")
print(f"{p*k}product of the numbers")
print(f"{p/k} is the quotient of the numbers")
#Performing String Concatenation
f= "Hello "
g=str(input("Enter your name "))
print(f"{f+g}")
#Dictionary
dict=[
    {
        "int": (x,y)
    },
    {
        "float":(p,k)
    },
    {
        "str": (f,g)
    }

]
print(dict)