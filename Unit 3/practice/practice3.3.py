answer = input("What is the capital of Minnesota?\n>> ")

answer = answer.lower()

if answer == "st. paul":
    print("Correct")
else:
    print("Wrong")



answer = input("Please enter a sentence.\n>> ")

print(answer.upper())
print(answer.strip())
print(answer.replace("bad", "good"))
print(answer.endswith("."))