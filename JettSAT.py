import json

## SpaceAI class to handle user credentials and save them to a file
class SpaceAI_login:
    def __init__(self):
        self.username = None
        self.password = None
        self.get_username = None
        self.get_password = None
        self.save_user_info = None

## Methods to get users username and store it
    def get_username(self):
        ('''the Get_Username method asks for the username of the user and stores it in the class variable self.username''')
        while True:
            username = input("Please enter your username: ")
            if not isinstance(username, str) or not username.strip():
                print("Invalid username. Please enter a valid string.")
            else:
                self.username = username
                if self.username is not None:
                    print(f"Welcome, {self.username}!")
                else:
                    print("username doesn't exist")
                return self.username

    ## Method to get users password and store it
    def get_password(self):
        ('''the Get_Password method asks for the password of the user and stores it in the class variable self.password''')
        while True:
            password = input("Please enter your password: ")
            if not isinstance(password, str) or not password.strip():
                print("Invalid password. Please enter a valid string.")
            else:
                self.password = password
                if self.password is not None:
                    print("Password accepted")
                else:
                    print("password doesn't exist")
                return self.password
    
    ## the file is so users can login later without having to enter their credentials again
    def save_user_info(self):
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
        # Input validation for filename and content
        if not isinstance(filename, str) or not filename.strip():
            print("Invalid filename. Please enter a valid string.")
            return
        if not isinstance(content, str):
            print("Invalid content. Please enter a valid string.")
            return
        with open("Questions_Answers.txt", "w") as file:
            file.write(content)
            if self.create_text_file is not None:
                print(f"{filename} created successfully.")
            else:
                print("file does not exist.")
        
    
## this method is the main method that handles asking questions and saving answers to the file   
    def ask_question(self):
        while True:
            question = input(" please enter the question you would like to ask? ")
            if not isinstance(question, str) or not question.strip():
                print("Invalid question. Please enter a valid string.")
            else:
                break
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
                while True:
                    add_answer = input("Would you like to add an answer for this question? (yes/no): ")
                    if add_answer.lower() not in ["yes", "no"]:
                        print("Please enter 'yes' or 'no'.")
                    else:
                        break
                if add_answer.lower() == "yes":
                    while True:
                        answer = input("Please enter the answer to this question: ")
                        if not isinstance(answer, str) or not answer.strip():
                            print("Invalid answer. Please enter a valid string.")
                        else:
                            break
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
    username = login.get_username()
    password = login.get_password()
    login.save_user_info()

('''after the user has logged in they will be taken to the menu where they can choose to ask a question or exit the program
if the user selects ask question the program will call the ask_question method
if the user selects exit the program will end''')

space_ai = SpaceAI()
filename = "Questions_Answers.txt"
while True:
    ## creates the text file before asking anyhting and going to the menu 
    space_ai.create_text_file(filename, content="") 
    while True:
        choice = input("Please choose an option from the menu (1-2): ")
        if choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 or 2.")
        else:
            break
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

















