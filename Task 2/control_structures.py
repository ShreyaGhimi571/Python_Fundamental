def classify_number():
#Using While Loop    
    while True:
        a=input("Enter a Number or type Exit to quit ")
        
#Code when user inputs "Exit"
        if a.lower()== "exit":
            break
#Code when User inputs a number    
        try:
            a=float(a)

            if a>0:
                
                print(f"{a} is positive a number")
            elif a<0:
                
                print(f"{a} is a negative number")
            else:
                
                print(f"{a} is 0")
#Code when User inputs a Invalid Value                
        except ValueError:
            
            print("Invalid Input")

#Calling the function
classify_number()
