#function
def passwords_weak():

#obtaining information
    password = input("Enter password:")

#easy passwords
    passwords = ['123456', 'password', '123456789', 'qwerty', '12345', '12345678', '111111', '1234567', '1234', 'Password1', '1234567890', 'letmein', 'qwerty123', 'admin' ]

#password check
    print("-Checking password-")
    result = password in passwords
    if result == True:
        print("The password is too simple, I recommend changing it")
    else:
        print("Strong password")