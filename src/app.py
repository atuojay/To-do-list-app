#This file contains the entry point to your tasks
# and the logic to manage it

from tasks import todo_list, create_task, delete_task, mark_as_finished,delete_all_tasks  # import other functions as well
from accounts import accounts, add_account, login  # import the function as well


if __name__ == "__main__":
    while True:
        print("Welcome to My To-do list!")
        print("Create your account!")
    
        name = input("Enter your name: ")
        password = input("Enter your password:")

        if name in accounts and password in accounts:
            login(name, password)
        else:
            add_account(name, password)

        #Allow a person to input a name and a password
    
        #Let the person sign in. If there details do not exist,
        #create an account for them
        if login(name, password) is True:
            while True:
                print("Select Option:")                  
                print("   1: Create Task")
                print("   2: Delete Task")
                print("   3: Delete all Tasks")
                print("   4: Mark Task as finished")

                selection = input("selection[1-4]: ")
        #Write code that implements the selected option
                if selection == '1':
                    create_task("task")
                elif selection == '2':
                    delete_task("task")
                elif selection == '3':
                    delete_all_tasks()
                elif selection == '4':
                    mark_as_finished("task")
                        
            else:
                print("Please register first!")
        
        else: 
            print("Please enter a new name and password to create your account")   
            add_account(name, password)
        
        