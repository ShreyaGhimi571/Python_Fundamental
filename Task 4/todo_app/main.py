
#Importing
from todo_operation import add_task, view_task, delete_task
from utils import usersays
tasks= []
#Using While loop
while True:
#MENU
    print("\nTo-do List\n")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")
    #Asking User for input
    opt=usersays("Enter what do you want to do:")
    opt=int(opt)
    

    if opt==1:
    #if user chooses to add
        add_task(tasks)
    
    elif opt==2:
    #if user chooses to view
        view_task(tasks)
    
    elif opt==3:
    #if user chooses to delete
        delete_task(tasks)


    elif opt==4:
    #if user chooses to exit
        break   

    else:
        print("Invalid Choice")
    









