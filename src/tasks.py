# This file contains code that manages your todo_list
todo_list = []

# Write a function creates a task
def create_task(task):
    task = input("Add task to list:")
    todo_list.append(task)
    return todo_list

# Write a function deletes a task
def delete_task(task):
    task = int(input("Enter position of task to delete:"))

    if task <= len(todo_list):
        todo_list.pop(task-1)
        return todo_list
    else:
        print("No task has been selected")
    
    #Removes the specified task from the todo_list

# Write a function that marks a task finished
def mark_as_finished(task):
    task = int(input("Enter position of finished task:"))

    if task <= len(todo_list):
        todo_list[task-1] + ' [finished]'
        return todo_list
    else:
        print("No task has been selected")

    #Append the string label '[finished]' at the end of the task 
    #if it does not already have the label appended.
    #It should remain in the todo_list

# Write a function deletes all tasks
def delete_all_tasks():
    todo_list.clear()

    #Empty the the todo_lsit
