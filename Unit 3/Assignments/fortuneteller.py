#   fortune teller named ChatGPT

print("Hello, I am ChatGPT\n" \
"I am fortune teller")

print("--------------------------------------")

lucky_int = input("What is your lucky interger?\n>> ")
future_float = input("How many years in the future would you like to see? May be a decimal number.\n>> ")
magical_mult_float = input("What is you magical multiplier?\n>> ")
ai_lvl_int = input("What A.I. level do you want? Higher intergers make riskier predictions (high risk, high reward).\n>> ")
num_float = input("Give me a number between 0 and 11:\n>> ")

def user_numbers():
    globals(lucky_int,future_float,magical_mult_float,ai_lvl_int,num_float)
    try:
        lucky_int = int(lucky_int)
        future_float = float(future_float)
        magical_mult_float = float(magical_mult_float)
        ai_lvl_int = int(ai_lvl_int)
        num_float = float(num_float)

        if future_float > 0:
            return
        else:
            print("Please enter a number actually in the future.")
            user_numbers()

        if num_float > 0 and num_float < 11:
            return
        else:
            print("Not between 0 and 11. Try again.")
            user_numbers()
    except:
        user_numbers()

import random
random_num = random.randint(-10, 10)
prediction_lvl = 0

if ai_lvl_int <= 3:
    if future_float < 1:
        if lucky_int == 7:
            prediction_lvl = 5
        elif lucky_int < 7:
            prediction_lvl = 3
        elif lucky_int <= 10:
            prediction_lvl = 4
        elif lucky_int < 100:
            prediction_lvl = 2
        else:
            prediction_lvl = 1
    elif future_float <= 5:
        if lucky_int == 7:
            prediction_lvl = 10

print(lucky_int + "\n" 
      + future_float + "\n" 
      + magical_mult_float + "\n" 
      + ai_lvl_int + "\n" 
      + num_float + "\n" 
      + str(random_num) + "\n" 
      + str(prediction_lvl) + "\n")

