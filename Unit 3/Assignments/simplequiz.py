x = 5
def tally_score():
    global x
    q = float(input("What's 1 + 1?\n>> "))
    if q == float(2):
        print("yis")
    else:
        print("nar")
    x = x-1
    if x > 0:
        tally_score()

tally_score()