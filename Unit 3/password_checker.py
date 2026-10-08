# We are going to make a program that behaves like a login screen
# the user enters a password
# if the password is correct, print "ACCESS GRANTED"
# otherwise, print "ACCESS DENIED"
# BONUS! If they get the password wrong, give them another chance to enter it an unlimited ammount of times
# SUPER BONUS: Limit them to three attempts before giving them the message "ACCOUNT LOCKED"


funi_password = "again"
real_password = "password"

password = input("Please enter your password\n>> ")
if password == real_password:
    print("ACCESS GRANTED!")
else:
    password = input("Your password is incorrect, please try again\n>> ")
    if password == real_password:
        print("ACCESS GRANTED!")
    else:
        password = input("Incorrect. Try again\n>> ")
        if password == real_password or password == funi_password:
            print("ACCESS GRANTED!")
        else:
            print("ACCESS DENITED!")