countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for count in countdown:
    print(count)

print("\n---------------------------------\n")

countdown.sort()
 #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in countdown:
    sum += num
print(sum)

print("\n---------------------------------\n")

intergers = [1, 2, 3, 4, 5]
# squared = [1, 4, 9, 16, 25]
for squ in intergers:
    print(squ * squ)

intergers = [1, 2, 3 ,4 ,5]
squares = []
for squ in intergers:
    squares.append(squ * squ)
print(squares)


print("\n---------------------------------\n")

word = input("Enter a word or phrase.\n>> ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = []
sum_vowel = 0
for vowel in vowels:
    if word.__contains__('a'):
        sum_vowel += 1
        vowel_count.insert(0, sum_vowel)
    print(vowel_count)


user_string = input(">> ")
vowel_sum = 0
for letter in user_string:
    if letter in ["a", "e", "i", "o", "u"]:
        vowel_sum += 1
print("Number of vowerls: " + str(vowel_sum))

print("\n---------------------------------\n")

user_number = int(input("Give me a number.\n>> "))
user_mult_table = []
if user_number < 10:
    ten = 10 - user_number
else:
    ten = 0
for i in range(1, user_number + 1 + ten, 1):
    user_mult_table.append(i)
for x in user_mult_table:
    print(str(user_number) + " x " + str(x) + " = " + str(user_number * x))


print("\n---------------------------------\n")

user_name = input("What's your name?\n>> ")
print("\n\n")
names = [user_name, "Osowski", "Taden", "Chase", "Chance", "Seth", "Christian", "Coooper Deee"]
for name in names:
    print("Hello, " + name + "!")
print("\n\n")