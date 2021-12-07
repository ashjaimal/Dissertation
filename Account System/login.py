'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register and login with user accounts for the project
'''


class user():
    def __int__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def login(self,username, password):
        self.username = input("ENTER USERNAME: ")
        self.password = input("ENTER PASSWORD: ")

        with open("register.txt", "r") as file:
            if username == username and password == password:
                print("LOGIN SUCCESSFUL")


    def register(self, username, password, email):
        self.username = input("ENTER USERNAME: ")
        self.password = input("ENTER PASSWORD: ")
        self.email = input("ENTER EMAIL: ")


        with open("register.txt" , "a") as file:
            file.write(username)
            file.write(password)
            file.write(email)







choice = int(input("OPTION 1: LOGIN\nOPTION 2: REGISTER"))
login1 = user()


if choice == 1:

    username = "user"
    password = "pass"

    login1.login(username, password)
elif choice ==2:

    username = "user"
    password = "pass"
    email = "as"

    login1.register(username, password,email)