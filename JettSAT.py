

import json


## SpaceAI class to handle user credentials and save them to a file
class SpaceAI:
    def __init__(self):
        self.username = None
        self.password = None

## Methods to get users username asks for for username and stores it in the class variable
    def Get_Username(self):
        username = input("Please enter your username: ")
        self.username = username
        return self.username
    ## Method to get users password asks for password and stores it in the class variable
    def Get_Password(self):
        password = input("Please enter your password: ")
        self.password = password
        return self.password
    
    ## This method creates a dictionary with the username and password and saves it to a file called "user_credentials.json"
    ## the file is so users can login later without having to enter their credentials again
    def Save_User_Info(self):
        user_credientials = {
            "username": self.username,
            "password": self.password
        }
        with open("user_credentials.json", "w") as file:
            json.dump(user_credientials, file)
        print("User credentials saved")
        