print("Welcome to the crate shop!" \
"\n") \

import random
bot = False
gainbot = False
spent = 0
gain = 0
cycle = 0

def net_worth():
    global spent
    global gain
    global gainbot
    global cycle
    net = spent + gain
    if net <= 0:
        cycle += 1
        gain_loss = "loss"
        if cycle == 500:
            print("Failed to earn money in 500 tries.")
            gainbot = False
            cycle = 0
    else:
        gain_loss = "gain"
        gainbot = False
    print(str(gain) + "$ earned"
    "\n" + str(net) + "$ net " + gain_loss)
    return gainbot

def crate():
    global bot
    global gainbot
    global spent
    global gain
    global cycle
    if not bot and not gainbot:
        global choice
        choice = input("\nWould you like to open a crate? ($5)" \
        "\n[Y/N]" \
        "\n>> ")
    elif bot:
        choice = "y"
    elif gainbot:
        choice = "y"
    choice = choice.lower()
    if choice == "y":                                                                                        
        chance = random.random()
        print("\n---------------------------------------\n")
        spent -= 5
        print(str(spent) + "$ lost\n")
        if chance <= .5:
            gain += 1
            print("You got a common...")
            net_worth()
            crate()
        elif chance <= (2/3):
            gain += 2
            print("You got an uncommon...")
            net_worth()
            crate()
        elif chance <= 0.85:
            gain += 5
            print("You got a rare!")
            net_worth()
            crate()
        elif chance <= 0.95:
            gain += 10
            print("You got a Super Rare!")
            net_worth()
            crate()
        else:
            gain += 25
            print("You got LEGENDARY!!")
            net_worth()
            bot = False
            crate()
    elif choice == "bot":
        print("\n(Secret bot is  on)\n")
        bot = True
        crate()
    elif choice == "winbot":
        print("\n(Net gain bot is on)\n")
        gainbot = True
        cycle = 0
        crate()
    elif choice == "n":
        print("You leave the shop.")
    else:
        print("INVALID" \
        "\nTry Again")
        crate()

crate()