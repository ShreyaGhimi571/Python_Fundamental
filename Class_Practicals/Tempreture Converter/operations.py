class temperature:
    def __init__(self,d_f):
        self.d_f=d_f
       
    def Celcius(self):
        C2F=(self.d_f*1.8)+32
        print(C2F," is the equivalent temperature in Farenheit")
    def Farenheit(self):
        F2C=(self.d_f-32)*1/1.8
        print(F2C," is the equivalent temperature in Celcius ")
        