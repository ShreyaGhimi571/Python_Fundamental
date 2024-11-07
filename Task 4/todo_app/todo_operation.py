#Function for adding Task
def add_task(tasks):
    task=input("Enter a task: ")
    tasks.append(task)
    print("Task is successfully added!")


#Function for viewing Task
def view_task(tasks):
    if not tasks:
        print("Tasks not Available")
    else:
#Using for loop for the index of tasks
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}: ")

#Function for deleting tasks
def delete_task(tasks):
    try:
        index=int(input("Enter the task number you want to delete: ")) -1
        del tasks[index]
        print("Task succesfully deleted")
    except IndexError:
        
        print("This is not a valid number")
    except ValueError:
        
        print("Please enter a number")





