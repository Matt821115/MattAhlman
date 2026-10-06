#   #1
name = input("What is your name?\n>> ")     #define variable "name"
loction = input("Where do you live?\n>> ") #define variable "location"
mood = input("How are you feeling?\n>> ")   #define variable "mood"

print("Hello " + name + " from " + loction + ". You are feeling " + mood + ".") #print final concatenation

print("\n------------------------------\n") #seperator

#   #2
def add_three(x, y, z): #create a function to print the sum of numbers
    print(float(x) + float(y) + float(z))

#define x, y, and z variables
x_input = input("x=")
y_input = input("y=")
z_input = input("z=")

add_three(x_input, y_input, z_input)

print("\n------------------------------\n") #seperators

#   #3
def data_three():   #create a function to define three variables and combine them as a string
    #variables to be defined
    word_input = input("Give me a word\n>> ")
    integer_input = int(input("Give me an integer\n>> "))
    float_input = float(input("Give me a float (decimal number)\n>> "))

    #print function, redfines integer to a float to add the integer and float numbers.
    print("You chose the word: " + word_input + ". And the sum of your two numbers is " + str(float(integer_input) + float_input) + ".")

data_three() #run function "data_three"
