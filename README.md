# Password Security Toolkit
### About the Project:
Password Security Toolkit is a Python - based console application designed for checking password security and generating new passwords.
It allows you to create passwords based on your specific criteria, assess their security, and compare them against a list of commonly
used passwords. You can also choose to have the security assessment results saved to a text file; for security reasons, the password 
itself will not be displayed.
### Features:
**Password strength checker** - analyzes the length of a password and the presence of various types of characters and digits. The
system provides recommendations on adding any missing elements. 

**Password generator** — creates random passwords based on parameters and character types selected by the user. You can generate
passwords up to 20 characters long by choosing any 4 parameters. 

**Check for common or weak passwords** — compares a password against a built-in list of frequently used, insecure passwords. If a 
match is found, the system recommends changing the password.

**A comprehensive password analysis** involves a series of checks, the results of which are saved in a text report. This file is 
updated with each new check. The report contains detailed information about the analysis performed, as well as recommendations 
for adding various types of characters and increasing the password's length. Furthermore, the password is compared against a list
of commonly used passwords; if a match is found, the system recommends changing it.
### Technologies used 
- Python 
- `Secrets` module for password generation 
- Standard Python libraries
### How to run the program:
1. Install Python. 
2. Download or clone the repository. 
3. Open a terminal in the project folder. 
4. Run the command: python main.py or python3 main.py.
### Project structure
Password-Security-Toolkit/

├── main.py

├── Modules/

│   ├── password_checker.py

│   ├── password_generator.py

│   ├── weak_passwords.py

│   └── security_report.py

├── README.md

└── .gitignore
### Limitations: 
1. The list of common weak passwords is limited and does not include all possible weak passwords. 
2. The strength assessment is simplified and does not guarantee a password's security; it only checks for password length and the
presence of various types of characters. 

3. This project is intended for educational purposes and is not a substitute for specialized password management tools.
### Author:
Rodin Irinarh Vadimovich 16 years old.

RIN