# This file contains code for managing your account

accounts = {}# dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    accounts[password] = name
    accounts.update({password:name})
    print(accounts)

def login(name, password):
    print("Login")
    name = input("Enter your name: ")
    password = input("Enter your password:")

    key, value = password, name
    
    if key in accounts and value == accounts[key]:
        return True
    else: 
        print("This username doesn't match with the password")
        return False

    
    #returns true if the password and corresponding name exist in the 
    #accounts dicitionary
    

