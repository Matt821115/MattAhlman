import random
print("\nWelcome to the Dungeons & Dragons based text adventure!\n\n")

#   currency/variables
gold = 100
drinks = 1

#   dice rolling
def roll_dice(d):
    roll = random.randint(1, d)
    return roll
#   character stats
stre = 8
intel = 8
wis = 8
const = 8
dex = 8
cha = 8
def stat_fix(stat):
    if stat > 20:
        stat = 20
        return stat
    else:
        return stat

def char_stats(stre_mod, intel_mod, wis_mod, const_mod, dex_mod, cha_mod):
    global stre
    global intel
    global wis
    global const
    global dex
    global cha
    global stre_bonus
    global intel_bonus
    global wis_bonus
    global const_bonus
    global dex_bonus
    global cha_bonus
    # stat updating
    stre = stat_fix(int(stre + stre_mod))
    intel = stat_fix(int(intel + intel_mod))
    wis = stat_fix(int(wis + wis_mod))
    const = stat_fix(int(const + const_mod))
    dex = stat_fix(int(dex + dex_mod))
    cha = stat_fix(int(cha + cha_mod))
    # stat bonuses
    stre_bonus = round((stre - 10) / 2)
    intel_bonus = round((intel - 10) / 2)
    wis_bonus = round((wis - 10) / 2)
    const_bonus = round((const - 10) / 2)
    dex_bonus = round((dex - 10) / 2)
    cha_bonus = round((cha - 10) / 2)
    # show player the stats
    print("Strength: " + str(stre) + 
          "\nIntelligence: " + str(intel) + 
          "\nWisdom: " + str(wis) + 
          "\nConstitution: " + str(const) + 
          "\nDexterity: " + str(dex) + 
          "\nCharisma: " + str(cha) + "\n")

#   classes
def fighter():
    print("Fighter stats updated")
    char_stats(7, 4, 4, 5, 5, 1)
    global gold
    gold = gold + 50
def barbarian():
    print("Barbarian stats updated")
    char_stats(9, 0, 1, 6, 2, -1)
    global gold
    gold = gold - 100
def wizard():
    print("Wizard stats updated")
    char_stats(2, 9, 7, 6, 3, 4)
    global gold
    gold = gold - 50
def rogue():
    print("Rogue")
    char_stats(4, 7, 7, 5, 8, 1)
    global gold
    gold = gold + 25
def cleric():
    print("Claric stats updated")
    char_stats(2, 7, 5, 4, 2, 5)
    global gold
    gold = gold + 100
def bard():
    print("Bard stats updated")
    char_stats(1, 6, 3, 3, 2, 8)
    global gold
    gold = gold + 75

#   races
def human():
    print("Human stats updated")
    char_stats(4, 2, 2, 1, 2, 2)
    global gold
    gold = gold + 25
def dwarf():
    print("Dwarf stats updated")
    char_stats(5, 3, 2, 5, 3, 1)
    global gold
    gold = gold - 25
def gnome():
    print("Gnome stats updated")
    char_stats(3, 6, 6, 4, 1, 4)
    global gold
    gold = gold - 75
def tiefling():
    print("Tiefling stats updated")
    char_stats(3, 6, 3, 4, 7, -3)
    global gold
    gold = gold -25
def dragonborn():
    print("Dragonborn stats updated")
    char_stats(9, 7, 7, 4, -1, -2)
    global gold
    gold = gold + 50
def sethling():
    print("Sethling stats updated")
    char_stats(2, -2, -4, 0, 0, 4)
    global gold
    gold = gold - 90

#   character template choosing
def choose_template():
    template = int(input("\nChoose a template" \
    "\n1 = Human Fighter" \
    "\n2 = Dwarf Barbarian" \
    "\n3 = Gnomish Wizard" \
    "\n4 = Tiefling Rogue" \
    "\n5 = Dragonborn Cleric" \
    "\n6 = Sethling Bard" \
    "\n>> "))
    print("")
    if template == 1:
        human()
        fighter()
    elif template == 2:
        dwarf()
        barbarian()
    elif template == 3:
        gnome()
        wizard()
    elif template == 4:
        tiefling()
        rogue()
    elif template == 5:
        dragonborn()
        cleric()
    elif template == 6:
        sethling()
        bard()
    else:
        print("IVALID INPUT TRY AGAIN\n")
        choose_template()
    print("You also start with " + str(gold) + " Gold.\n")

# class choice for custom character
def dnd_classe(clas):
    if clas == 1:
        return fighter()
    elif clas == 2:
        return barbarian()
    elif clas == 3:
        return wizard()
    elif clas == 4:
        return rogue()
    elif clas == 5:
        return cleric()
    elif clas == 6:
        return bard()
    else:
        return

#   custom character choosing
def choose_custom():
    print("\nPick a race" \
    "\n1 = Human" \
    "\n2 = Dwarf" \
    "\n3 = Gnome" \
    "\n4 = Tiefling" \
    "\n5 = Dragonborn" \
    "\n6 = Sethling")
    species = int(input(">> "))
    print("\nPick a class" \
    "\n1 = Fighter" \
    "\n2 = Barbarian" \
    "\n3 = Wizard" \
    "\n4 = Rogue" \
    "\n5 = Cleric" \
    "\n6 = Bard")
    dnd_class = int(input(">> "))
    if species == 1:
        human()
    elif species == 2:
        dwarf()
    elif species == 3:
        gnome()
    elif species == 4:
        tiefling()
    elif species == 5:
        dragonborn()
    elif species == 6:
        sethling()
    else:
        choose_custom()
    dnd_classe(dnd_class)
    print("You also start with " + str(gold) + " Gold.\n")

#   tavern story
def tavern():
    global gold
    global drinks
    global intel_bonus
    global wis_bonus
    global stre_bonus
    tab = 10 * drinks
    print("\nYou may:" \
    "\nPAY your tab" \
    "\nOrder ANOTHER round" \
    "\nAttempt to FLEA without paying your tab")
    choice = input(">> ").lower()
    alcohol_toxicity = drinks / 5
    if alcohol_toxicity >= 5:
        print("\nYou have too much alcohol in you."
        "\nYou die from alcohol poisoning.\n")
        return
    elif alcohol_toxicity == 4:
        intel_bonus = intel_bonus - 4
        wis_bonus = wis_bonus - 3
        stre_bonus = stre_bonus - 2
    elif alcohol_toxicity == 3:
        intel_bonus = intel_bonus - 3
        wis_bonus = wis_bonus - 2
        stre_bonus = stre_bonus - 1
    elif alcohol_toxicity == 2:
        intel_bonus = intel_bonus - 2
        wis_bonus = wis_bonus - 1
    elif alcohol_toxicity == 1:
        intel_bonus = intel_bonus - 1
    else:
        print()
    if choice == "pay":
        if gold >= tab:
            gold = gold - tab
            print("You pay " + str(gold) + "Gold for " + str(drinks) + "drinks."
            "\nYou now have " + str(gold) + "Gold.")
        else:
            print("You cannot pay your tab. You may attempt to flea.")
            tavern()
    elif choice == "another":
        print("\nYou order another round.")
        drinks = drinks + 1
        tab = 10 * drinks
        print("Your tab is now " + str(tab) + " gold, for " + str(drinks) + " drinks."
        "\nYou have " + str(gold) + " Gold.")
        tavern()

#   start up
def DnD():
    print("You start your adventure in a tavern like many other adventures." \
          "\nBut first, you must create your character.\n")
    char = input("Would you like to create a custom character or use a template?" \
                 "\nEnter CUSTOM for a custom character" \
                 "\nEnter TEMPLATE for a character template" \
                 "\n>> ")
    char = char.lower()
    if char == "custom":
        choose_custom()
    elif char == "template":
        choose_template()
    else:
        print("INVALID INPUT TRY AGAIN\n")
        DnD()
    print("And so your story starts here. All choices with text input are CAPITALS." \
    "\nYou may leave the tavern as you choose." \
    "\nMake sure to pay your tab before you leave. :)")
    tavern()

DnD()
