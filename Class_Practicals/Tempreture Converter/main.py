from operations import temperature

d_f=float(input("Enter the tempreture"))
opt=input("Enter C if the entered value is Celcius\nEnter F if the entered value is Farenheit: ")


temp=temperature(d_f)
if opt.lower()== "c":
    temp.Celcius()
elif opt.lower()=="f":
    temp.Farenheit()
else:
    print("Invalid Input")




