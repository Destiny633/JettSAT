

import json


## SpaceAI class to handle user credentials and save them to a file
class SpaceAI_login:
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



class SpaceAI:
    def __init__(self):
        self.ask_question = None
        self.add_question_answer = None
        self.create_text_file = None

## this method creates a text file with the given filename and content        

    def create_text_file(self, filename, content=""):
        with open("Questions_Answers.txt", "w") as file:
            file.write(content)
        
    
## this method asks the user a questions and checks if the question has an answer
## by reading the Questions_Answers.txt file    
    def ask_question(self):
        question = input(" please enter the question you would like to ask? ")
        found = False
        ## check if the question has an answer Questions_Answers.txt
        try:    
            with open("Questions_Answers.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 2):
                    if lines[i].strip() == question:
                        print("Answer:", lines[i+1].strip())
                        found = True 
                        break
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


            

        
    
if __name__ == "__main__":
    print("Welcome to SpaceAI!")
    print("Please login to continue.")
    login = SpaceAI_login()
    username = login.Get_Username()
    password = login.Get_Password()
    login.Save_User_Info()


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
        





     

        

        






        