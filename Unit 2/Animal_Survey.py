print("Welcome to the Animal Survey")

fav_animal = input("What is your favorite animal?\n>> ") #first of many questions
owned_animal = input("If you own an animal, what is it?\n>> ")
why_fav_anim = input("Why is " + fav_animal + " your favorite animal?\n>> ")
sound_fav_anim = input("What sound do " + fav_animal + "s make?\n>> ")
live_fav_anim = input("Where do " + fav_animal + "s live?\n>> ")
color_fav_anim = input("what color or colors are " + fav_animal + "s?\n>> ")

print("Wow! So intresting!") #reaction
fun_fact = input("What's a fun fact you about the " + fav_animal + "?\n>> ") #final questions
diet_fav_anim = input("What do " + fav_animal + "s eat?\n>> ")

print("That's so cool!") #final reaction before summary
#summary here ↓↓↓
print("So your favorite animal is " + fav_animal + ". Which lives in " + live_fav_anim + ". Where they eat " + diet_fav_anim + ". You like " + fav_animal + "s because " + why_fav_anim + ". They are colored " + color_fav_anim + ". And the make the sound " + sound_fav_anim + ".")

