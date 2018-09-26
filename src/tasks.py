# This file contains code that manages your todo_list
todo_list = []

# Write a function creates a task
def create_task(task):
    task = input("Add task to list:")
    todo_list.append(task)
    print(todo_list)

# Write a function deletes a task
def delete_task(task):
    task = input("Enter position of task to delete:")

    if task.isdigit() and int(task) <= len(todo_list):
        todo_list.pop(int(task)-1)
        print(todo_list)
    else:
        print("No task has been selected")

# Write a function that marks a task finished
def mark_as_finished(task):
    task = input("Enter position of finished task:")

    if task.isdigit() and int(task) <= len(todo_list):
        todo_list[int(task)-1] += ' [finished]'
        print(todo_list)
    else:
        print("No task has been selected")

# Write a function deletes all tasks
def delete_all_tasks():
    todo_list.clear()
    print(todo_list)


