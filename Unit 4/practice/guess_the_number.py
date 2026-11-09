import random

def gtn():
    guesses = 0
    ran_num = random.randint(1, 100)
    guessed = False
    print("Guess the random number!" \
    "\n[1 - 100]")
    while guessed == False:
        if guesses == 1:
            rank = "INCONCEIVABLE!!"
        elif guesses >= 2:
            rank = "INSANE!"
        elif guesses > 3:
            rank = "Platinum!"
        elif guesses > 5:
            rank = "Gold"
        elif guesses > 10:
            rank = "Silver"
        elif guesses > 20:
            rank = "bronze"
        elif guesses > 50 and guesses <=100:
            rank = "Seth"
        else:
            rank = "how?"
        def guess():
            global user_guess
            user_guess = input("Your guess" \
            "\n>> ")
            try:
                user_guess = int(user_guess)
            except:
                print("INVALID")
                guess()
        guess()
        guesses += 1
        if user_guess > ran_num:
            print("\n------\n" \
            "Lower")
        elif user_guess < ran_num:
            print("\n------\n" \
            "Higher")
        elif user_guess == ran_num:
            guessed = True
            user_input = input("\n------\n" \
            "Correct! Done in " + str(guesses) +
            "\nRanked: " + rank + \
            "\n" \
            "\nWant to play again?" \
            "\n[Y/N]" \
            "\n" \
            "\n>> ")
            user_input = user_input.lower()
            if user_input == "y":
                print("\n--------------------------------------------------\n" \
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                gtn()
            elif user_input == "n":
                print("Goodbye")
            else:
                print("Invalid input" \
                "\nDetermining as quit")
gtn()