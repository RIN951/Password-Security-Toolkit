#libraries
import string

#function
def check_password_strength():

#obtaining information
    password = input('Enter password:')

#variables
    score = 0
    recommendations = []

#password analysis and information output
    print("-Password analysis-")
    length = len(password)
    print("Length:", length, "characters")
    if length >= 12:
        score =+ 1
    else:
        recommendations.append("-Add more characters (at lest 12)")
    lowercase = any(char.islower() for char in password)
    if lowercase == True:
        print("Lowercase letters: yes")
        score += 1
    else:
        print("Lowercase letters: no")
        recommendations.append("-Add lowercase letters")
    uppercase = any(char.isupper() for char in password)
    if uppercase == True:
        print("Uppercase letters: yes")
        score += 1
    else:
        print("Uppercase letters: no")
        recommendations.append("-Add uppercase letters")
    numbers = any(char.isdigit() for char in password)
    if numbers == True:
        print("Numbers: yes")
        score += 1
    else:
        print("Numbers: no")
        recommendations.append("-Add the numbers")
    special = any(char in string.punctuation for char in password)
    if special == True:
        print("Special characters: yes")
        score += 1
    else:
        print("Special characters: no")
        recommendations.append("-Add special characters")

#result
    if score == 5:
        print("Result: password strong")

    elif score == 3 or score == 4:
        print("-Result: password fair- \nRecommendations:", *recommendations, sep='\n')

    elif score <= 2:
        print("-Result: password weak- \nRecommendations:", *recommendations, sep='\n')