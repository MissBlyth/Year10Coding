### Access Denied
attempts = 3

while attempts > 0:
    #get username
    username = input("Username:")
    #get password
    password = input("Password:")

    #compare username to BLY and password to 12345
    #output access result
    if username=="BLY" and password == "12345":
        print("Access Granted")
        break

    elif username=="QTA" and password == "54321":
        print("Access Granted")
        break

    else:
        print("Access Denied")
        attempts -= 1

