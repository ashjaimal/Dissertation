#import mysql

def register():
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    passwordCheck = input("ENTER PASSWORD AGAIN: ")

    while password != passwordCheck:
        print("PASSWORDS DO NOT MATCH\nENTER PASSWORD AGAIN")
        password = input("ENTER PASSWORD: ")
        passwordCheck = input("ENTER PASSWORD AGAIN: ")

    age = int(input("ENTER AGE: "))
    gender = input("ENTER GENDER: ")

    print("REGISTER COMPLETE")


register()