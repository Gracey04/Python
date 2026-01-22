username = input("Enter your name: ")
password = input("Enter password: ")

#Username
if username != username.strip():
    print("remove extra spaces")
elif username[0].islower == username:
    print("Username must start with a capital letter")
elif username[1:].isupper == username:
    print("Incorrect password")
else:
    print("Username accepted")

#Password
if password != password.strip():
    print("remove extra space")
elif password[0].islower == username:
    print(" password must start with capital letter")
else:
    print("password accepted")