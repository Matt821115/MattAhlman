print("Amazon Prime subscription\n\nTo purchase the yearly " \
"subscription for $139.99 you must:\n>Be 18 years of age or " \
"older*\n>Have a valid bank account\n>Have enough money for the " \
"first year\n*(unless permitted by an adult)")

print("\n------------------------------------------------------\n")

eligable = "test"
user_age = int(input("How old are you?\n>> "))
if user_age < 18:
    permitted = input("Were you permitted to make this purchase by" \
    " an adult?\n>> ")
    if permitted.lower() == "y" or permitted.lower() == "yes":
        eligable = bool(True)
    else:
        eligable = bool(False)
else:
    eligable = bool(True)

print(eligable)