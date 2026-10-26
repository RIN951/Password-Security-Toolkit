#libraries
import string
import secrets

#function
def generate_password():

#variables
    password = []
    score = 0
    selected_parameters = str()
    negative_score = 0

#obtaining information
    while True:
        length_numbers = input("Enter password length:")
        if length_numbers.isdigit():
            length = int(length_numbers)
            if length > 0 and length <= 20:
                break
            else:
                print("Errors: enter a number greater than 0 and less than 21")
        else:
            print("Error: enter a positive number")
    while True:
        lowercase = input("Include lowercase letters? (y/n):")
        if lowercase == "y":
            password.append(secrets.choice(string.ascii_lowercase))
            score += 1
            selected_parameters += string.ascii_lowercase
            break
        elif lowercase == "n":
            negative_score += 1
            break
        else:
            print("Error: enter y or n")
    while True:
        uppercase = input("Include uppercase letters? (y/n):")
        if uppercase == "y":
            password.append(secrets.choice(string.ascii_uppercase))
            score += 1
            selected_parameters += string.ascii_uppercase
            break
        elif uppercase == "n":
            negative_score += 1
            break
        else:
            print("Error: enter y or n")
    while True:
        number = input("Include numbers? (y/n):")
        if number == "y":
            password.append(secrets.choice(string.digits))
            score += 1
            selected_parameters += string.digits
            break
        elif number == "n":
            negative_score += 1
            break
        else:
            print("Error: enter y or n")
    while True:
        special = input("Include special character? (y/n):")
        if special == "y":
            password.append(secrets.choice(string.punctuation))
            score += 1
            selected_parameters += string.punctuation
            break
        elif special == "n":
            negative_score += 1
            break
        else:
            print("Error: enter y or n")

#generated password and parameter verification
    print("-Generated password-")
    choice = length - score
    if negative_score == 4:
        print("Error: select at least 1 parameter")
        generate_password()
    else:
        pass
    if choice < 0:
        print("Error: write a greater number of characters")
        generate_password()
    else:
        pass
    for i in range(choice):
        password.append(secrets.choice(selected_parameters))
        secrets.SystemRandom().shuffle(password)

#password output
    print("Password:", *password, sep="")