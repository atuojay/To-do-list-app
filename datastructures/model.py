todo_list = {}

def create_list(list_title):
    todo_items = []
    list_title = input("Create New List: ")
    todo_list[list_title] = todo_items
    print(todo_list)

def add_items(list_title, items):
    list_title = input("Enter title of list to add task to: ")

    if list_title in todo_list.keys():
        items = input("Enter item to list:")
        todo_list[list_title].append(items)
        print(todo_list)
    else:
        print("This list was not found")

def find_list_item(list_title, items):
    list_title = input("Enter title of list where task is: ")

    if list_title in todo_lists.keys():
        list_items = todo_lists.get(list_title)
        print(list_items)
        item = int(input("Enter task postion to find in the list: "))
        if item <= len(list_items) and type(items) == int:
            print(list_items[item-1])
            return todo_lists
        else:
            print("That task is unknown or isn't in this list")
            return False
        return todo_lists

    else:
        print("The list {0} was not found ".format(list_title))

def delete_item(list_title, items):
    list_title = input("Enter title of list to delete task from: ")

    if list_title in todo_lists.keys():
        list_items = todo_lists.get(list_title)
        print(list_items)
        item = int(input("Enter task postion to delete in the list: "))
        
        if item < len(list_items) and type(item) == int:
            del (list_items[item-1])
            return todo_lists
        else:
            print("That task is unknown or isn't in this list")
            return False
        return todo_lists

    else:
        print("The list {0} was not found".format(list_title))
        return False

def edit_list_item(list_title, items):
    list_title = input("Enter title of list where task is: ")

    if list_title in todo_lists.keys():
        list_items = todo_lists.get(list_title)
        print(list_items)
        item = int(input("Enter task postion to edit in the list: "))

        if item <= len(list_items) and type(item) == int:
            edited = input("Edited task: ")
            list_items.remove(list_items[item-1])
            list_items.insert(item-1, edited)
            return todo_lists
        else:
            print("That task is unknown or isn't in this list")
            return False
        return todo_lists

    else:
        print("The list {0} was not found".format(list_title))
        return False

def clear_list_items(list_title):
    list_title = input("Enter title of list to empty: ")

    if list_title in todo_lists.keys():
        list_items = todo_lists.get(list_title)
        list_items.clear()
        return todo_lists

    else:
        print("The list {0} was not found".format(list_title))
        return False

def delete_todo_list(list_title):
    list_title = input("Enter title of list to delete: ")

    if list_title in todo_lists.keys():
        del todo_lists[list_title]
        return todo_lists

    else:
        print("The list {0} was not found".format(list_title))
        return False

    
