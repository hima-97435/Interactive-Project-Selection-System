# Author name -- > Himanshu Pokhriyal
# Version -- 3.12.1
# Author name -- > Himanshu Pokhriyal
# Version -- 3.12.1
import os
from getpass import getpass


# Define a function to check if the entered username and password match the ones in the file
def check_credentials(username, password):
    with open("password_manager.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            # Skip the line if it doesn't contain a comma
            if "," not in line:
                continue
            user, passw = line.strip().split(",")
            if username == user and password == passw:
                return True
    return False


# Define a function to check if a username is already taken
def is_username_taken(username):
    with open("password_manager.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            # Skip the line if it doesn't contain a comma
            if "," not in line:
                continue
            user, _ = line.strip().split(",")
            if username == user:
                return True
    return False

# Define a function to register a new user
def register_user(username, password):
    with open("password_manager.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            # Skip the line if it doesn't contain a comma
            if "," not in line:
                continue
            existing_user, existing_pass = line.strip().split(",")
            if username == existing_user:
                if password == existing_pass:
                    print("This account already exists.")
                else:
                    print("This username is already taken and the password does not match the existing account. Please try a different username.")
                return False
    with open("password_manager.txt", "a") as file:
        file.write(f"{username},{password}\n")
    return True

# Ask the user to login or register
while True:
    print("Please login or register to continue.")
    action = input("Do you want to login or register? (login/register): ")
    if action.lower() == "login":
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")

        # Check if the entered credentials are correct
        if check_credentials(username, password):
            print("Login successful!")
            break
        else:
            print("Invalid username or password.")
    elif action.lower() == "register":
        username = input("Enter a username for your new account: ")
        password = getpass("Enter a password for your new account: ")

        # Register the new user
        if register_user(username, password):
            print("Registration successful! You can now login with your new account.")
            break
        else:
            print("Registration failed. Please try again.")
    else:
        print("Invalid action. Please enter 'login' or 'register'.")
print("👋 Welcome to the Fun Project Menu!")

    
        # Rest of your code...
print("Choose a project to work on:")

print("Here are the available projects:")
print("1. Simple Quiz")
print("2. Number Guessing Game")
print("3. Rock Paper Scissors")

file_name = "project_description.txt"

    # Check if the file exists
if os.path.isfile(file_name):
        # Open the file in VS Code

    os.system(f'code {file_name}')
        # print(f"Opened '{file_name}' in VS Code.")
else:
    print(f"'{file_name}' not found in the current directory.")


project_files = {
        1: "simple_quiz_description.txt",
        2: "number_guessing_description.txt",
        3: "rock_paper_scissors_description.txt"
    }

code_files = {
        1: "code_of_simple_quiz.txt",
        2: "code_of_number_guessing.txt",
        3: "code_of_rock_paper.txt"
    }

while True:
        try:
            project_number = int(input("Please enter the number of the project you want to work on: "))
            if project_number in project_files.keys():
                # Get the file name corresponding to the chosen project number
                file_name = project_files[project_number]
                # Check if the file exists
                if os.path.isfile(file_name):
                    # Open the file in VS Code
                    os.system(f'code {file_name}')
                    

                    # Ask if the user wants to create a .py file
                    create_py_file = input("Do you want to create a .py file for this project? (yes/no): ")
                    if create_py_file.lower() == "yes":
                        # Read code from the correct code file and create a new .py file
                        with open(code_files[project_number], "r") as code_file:
                            code_content = code_file.read()
                        with open(f"project_code_{project_number}.py", "w") as py_file:
                            py_file.write(code_content)
                        print(f"Created 'project_code_{project_number}.py' with code from '{code_files[project_number]}'.")
                    break
                else:
                    print(f"'{file_name}' not found in the current directory.")
            else:
                print("Invalid selection. Please enter a valid project number (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
