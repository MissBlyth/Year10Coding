### Access Denied
#get username
username = input("Username:")
#get password
password = input("Password:")

#compare username to BLY and password to 12345
#output access result
if username=="BLY" and password == "12345":
    print("Access Granted")
else:
    print("Access Denied")
