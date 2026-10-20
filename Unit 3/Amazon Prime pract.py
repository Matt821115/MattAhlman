print("Amazon Prime subscription\n\nTo purchase the yearly " \
"subscription for $139.99 you must:\n>Be 18 years of age or " \
"older*\n>Have a valid bank account\n>Have enough money for the " \
"first year\n*(unless permitted by an adult)")

print("\n------------------------------------------------------\n")

eligable = bool(False)
user_age = int(input("How old are you?\n>> "))
if user_age < 18:
    permitted = input("Were you permitted to make this purchase by" \
    " an adult?\n>> ")
    if permitted.lower() == "y" or permitted.lower() == "yes":
        eligable = True
    else:
        eligable = False
else:
    eligable = True

# print(eligable)
if eligable == True:
    bal = float(input("What is your current bank balence?\n>> $"))

    if bal >= 139.99:
      print("You have subscribed to Amazon Prime!")
    else:
        print("We're sorry, you don't have enough money for this subscription")
else:
    print("I'm sorry, you cannot purchase the subscription.")