'''
@Author: Ashwin Jaimal
@Date: 03/12/2021
@About: Login Registration System
'''

import csv

#Function to allow users to register user accounts
def register():
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    passwordCheck = input("ENTER PASSWORD AGAIN: ")
    email = input("ENTER EMAIL: ")
    age = int(input("ENTER AGE: "))

    accounts = [username,password,email,age]

    while password != passwordCheck:
        print("PASSWORDS DO NOT MATCH\nTRY AGAIN")

        password = input("ENTER PASSWORD: ")
        passwordCheck = input("ENTER PASSWORD AGAIN: ")



    with open ('accounts.csv' , 'a' , encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(accounts)




register()