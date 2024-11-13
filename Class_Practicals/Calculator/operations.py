import math
class Arithmetic_Operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print(f"{self.a+self.b} is the sum of the given numbers")
    def subtraction(self):
        print(f"{self.a-self.b} is the difference of the given numbers")

    def multiply(self):
        print(f"{self.a*self.b} is the product of the given numbers")

    def division(self):
        try:
            print("Second Number cant be zero")
        except:
            print(f"{self.a/self.b} is the quotient of the given numbers")

class Scientific():
    def sin(self,a):
        print(math.sin(a))
    def cos(self,a):
        print(math.cos(a))
    