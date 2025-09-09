

import json


## SpaceAI class to handle user credentials and save them to a file
class SpaceAI_login:
    def __init__(self):
        self.username = None
        self.password = None

## Methods to get users username and store it
    def Get_Username(self):
        ('''the Get_Username method asks for the username of the user and stores it in the class variable self.username''')
        username = input("Please enter your username: ")
        self.username = username
        return self.username
    ## Method to get users password and store it
    def Get_Password(self):
        ('''the Get_Password method asks for the password of the user and stores it in the class variable self.password''')
        password = input("Please enter your password: ")
        self.password = password
        return self.password
    
    ## the file is so users can login later without having to enter their credentials again
    def Save_User_Info(self):
        ('''the Save_User_Info method creates a dictionary with the username and password and saves it to a file called "user_credentials.json"''')
        user_credientials = {
            "username": self.username,
            "password": self.password
        }
        with open("user_credentials.json", "w") as file:
            json.dump(user_credientials, file)
        print("User credentials saved")


## this is the main class that handles the functionality of the program for the SpaceAI
class SpaceAI:
    def __init__(self):
        self.ask_question = None
        self.create_text_file = None

## this method creates a text file with the name Questions_Answers.txt for data to be saved too     

    def create_text_file(self, filename, content=""):
        ('''the create_text_file method creates a new text file with the given name Questions_Answers.txt and writes the content to it''')
        with open("Questions_Answers.txt", "w") as file:
            file.write(content)
        
    
## this method is the main method that handles asking questions and saving answers to the file   
    def ask_question(self):
        question = input(" please enter the question you would like to ask? ")
        found = False
        ('''the ask_question method reads the Questions_Answers.txt file and checks if the question has an answer
        by reading the file line by line and checking if the question is in the file and if the question is found it will print the answer''')
        try:
            with open("Questions_Answers.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 2):
                    if lines[i].strip() == question:
                        print("Answer:", lines[i+1].strip())
                        found = True 
                        break

            ('''if the question or answer is not found it will ask the user if they would like to save the question and answer to the file
            if the user says yes it will ask for the answer and save it to the file
            if the user says no it will not save the question and answer to the file''')
            
            if not found:
                print("Sorry, i dont have an answer for that question.")
                add_answer = input("Would you like to add an answer for this question? (yes/no): ")
                if add_answer.lower() == "yes":
                    answer = input("Please enter the answer to this question: ")
                    with open("Questions_Answers.txt", "a") as file:
                        file.write(question + "\n")
                        file.write(answer + "\n")
                    print("Question and answer have been added.")
                else:
                    print("question and answer will not be added.")
        except FileNotFoundError:
            print("Questions_Answers.txt file not found. Please create the file first.")


            

        
## this is the main function that logs the user in and runs the program and displays the menu 
('''the function will create an instance of the SpaceAI_login class and ask the user for their username and password
it will then save the user credentials to a file''')
if __name__ == "__main__":
    print("Welcome to SpaceAI!")
    print("Please login to continue.")
    login = SpaceAI_login()
    username = login.Get_Username()
    password = login.Get_Password()
    login.Save_User_Info()

('''after the user has logged in they will be taken to the menu where they can choose to ask a question or exit the program
if the user selects ask question the program will call the ask_question method
if the user selects exit the program will end''')

space_ai = SpaceAI()
filename = "Questions_Answers.txt"
while True:
    ## creates the text file before asking anyhting and going to the menu 
    space_ai.create_text_file(filename, content="") 
    choice = input("Please choose an option from the menu (1-2): ")
    print("\nMenu:")
    print("1. Ask a question")
    print("2. Exit")
    if choice == "1":
        space_ai.ask_question()
    elif choice == "2":
        print("Thank you for using SpaceAI. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        





     

        

        






        