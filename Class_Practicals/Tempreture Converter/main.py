from operations import temperature

d_f=float(input("Enter the temperature"))
opt=input("Is the entered temperature farenheit or degree: ")


temp=temperature(d_f)
if opt.lower()== "celcius":
    temp.Celcius()
elif opt.lower()=="farenheit":
    temp.Farenheit()
else:
    print("Invalid Input")




