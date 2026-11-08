#while loop password

from getpass import getpass

islogin = False
loginattempt = 0

u = "user"
p = "123"

while islogin == False:
    uname = input("Input your user:")
    pword = getpass("Input your password:")

    if uname == u and pword == p:
        print("User logged in")
        print("Total attempt:",loginattempt)
        islogin = True
        break

    else:
        print("Incorrect username and password")
        loginattempt += 1
        print("Total attempt:",loginattempt)
        islogin = False
        continue