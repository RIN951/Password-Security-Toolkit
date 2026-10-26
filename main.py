#function binding
from Modules.password_checker import check_password_strength
from Modules.password_generator import generate_password
from Modules.weak_passwords import passwords_weak
from Modules.security_report import report_security

#menu
while True:
    print("===PASSWORD SECURITY TOOLKIT V1.0===")
    print("1. Check password strength")
    print("2. Generate password")
    print("3. Check common weaknesses")
    print("4. Full password analysis and save security report")
    print("5. Exit")

#menu setting
    while True:
        try:
            chores = int(input("Select an action:"))
            if chores > 0 and chores < 6:
                break
            print("Error: Enter a number from 1 to 5")
        except ValueError:
            print("Error: Enter a integer")

#execution of actions
    if chores == 1:
        print("=CHECK PASSWORD STRENGTH=")
        #password_checker.py
        check_password_strength()
    if chores == 2:
        print('=GENERATE PASSWORD=')
        #password_generator.py
        generate_password()
    if chores == 3:
        print("=CHECK COMMON WEAKNESSES=")
        #weak_passwords.py
        passwords_weak()
    if chores == 4:
        print("=FULL PASSWORD ANALYSIS AND SAVE SECURITY REPORT=")
        #security_report.py
        report_security()
    if chores == 5:
        print("Goodbye!")
        break