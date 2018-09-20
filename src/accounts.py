# This file contains code for managing your account

accounts = {}# dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    name = input("Enter your name: ")
    password = input("Enter your password:")
    accounts[password] = name
    accounts.update({password:name})
    return accounts


def login(name, password):
    for key,value in accounts.items():
        if key == password and value == name:
            return True
        else 
            print("This username doesn't match with the password")
    else
        add_account(name, password)
    
    
    #returns true if the password and corresponding name exist in the 
    #accounts dicitionary
    

