#libraries
import string
import os
import platform

def report_security():
#owerwrite the file
    with open("Reports.txt", "w", encoding="utf-8") as file:
        file.write("=Password Security Reports=\n")

#obtaining information
    password = input('Enter password:')

#variables
    score = 0
    recommendations = []

#password analysis and information output
    length = len(password)
    with open("Reports.txt", "a", encoding="utf-8") as file:
        file.write("Length: " + str(length) + " characters\n")
    if length >= 12:
        score =+ 1
    else:
        recommendations.append("-Add more characters (at lest 12)")
    lowercase = any(char.islower() for char in password)
    if lowercase == True:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Lowercase letters: yes\n")
        score += 1
    else:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Lowercase letters: no\n")
        recommendations.append("-Add lowercase letters")
    uppercase = any(char.isupper() for char in password)
    if uppercase == True:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Uppercase letters: yes\n")
        score += 1
    else:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Uppercase letters: no\n")
        recommendations.append("-Add uppercase letters")
    numbers = any(char.isdigit() for char in password)
    if numbers == True:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Numbers: yes\n")
        score += 1
    else:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Numbers: no\n")
        recommendations.append("-Add the numbers")
    special = any(char in string.punctuation for char in password)
    if special == True:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Special characters: yes\n")
        score += 1
    else:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("Special characters: no\n")
        recommendations.append("-Add special characters")

#result
    if score == 5:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("-Result: password strong-\n")

    elif score == 3 or score == 4:
            with open("Reports.txt", "a", encoding="utf-8") as file:
                file.write("-Result: password fair- \nRecommendations:\n")
            with open("Reports.txt", "a", encoding="utf-8") as file:
                for word in recommendations:
                    file.write(word + "\n")

    elif score <= 2:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("-Result: password weak- \nRecommendations:\n")
        with open("Reports.txt", "a", encoding="utf-8") as file:
            for word in recommendations:
                file.write(word + "\n")


#easy passwords
    passwords = ['123456', 'password', '123456789', 'qwerty', '12345', '12345678', '111111', '1234567', '1234', 'Password1', '1234567890', 'letmein', 'qwerty123', 'admin' ]

#password check
    result = password in passwords
    if result == True:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("-Checking password-\nThe password is too simple, I recommend changing it")
    else:
        with open("Reports.txt", "a", encoding="utf-8") as file:
            file.write("-Checking password-\nStrong password")

#info
    print("The file is located: Password-Security-Toolkit/Reports.txt")

#open file
    file = "Reports.txt"
    if platform.system() == "Windows":
        os.startfile(file)
    elif platform.system() == "Linux":
        os.system(f"xdg-open {file}")