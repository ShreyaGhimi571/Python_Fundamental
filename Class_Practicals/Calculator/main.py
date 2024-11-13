from operations import Arithmetic_Operations,Scientific
#user prompt
opt=int(input("Enter 1 if you want to perform arithmetic operation\n2 if you want to perform scientific: "))
if(opt==1):
    a=float(input("Enter first number: "))
    b=float(input("Enter second Number: "))

    choice=int(input("Input 1 to add\nInput 2 to subtract\nInput 3 to multiply\nInput 4 to divide "))
    at=Arithmetic_Operations(a,b)
    if choice==1:
        at.addition()
    elif choice==2:
        at.subtraction()
    elif choice==3:
        at.multiply()
    elif choice==4:
        at.division()
    else:
        print("Invalid Input")
elif(opt==2):
    a=float(input("Enter the number"))
    choice=int(input("Input 1 to use Sin\t2 to use cosine"))
    st=Scientific()
    if choice==1:
        st.sin(a)
    elif choice==2:
        st.cos(a)
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice")

    