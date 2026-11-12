student_data = { # wrong
    "name": "Chase",
    "age": 17,
    "grade": "A",
    "name": "Chance",
    "age": 17,
    "grade": "A",
    "name": "Seth",
    "age": 16,
    "grade": "F",
    "name": "Taden",
    "age": 17,
    "grade": "C",
    "name": "Will",
    "age": 15,
    "grade": "B"
}

for student in student_data:
    print(student + ": " + str(student_data[student]))

print("\n---------------------------------\n")

student_data = {
    "Chase": "A",
    "Chance": "A-",
    "Seth": "F",
    "Taden": "C",
    "Will": "B"
}
for student in student_data:
    print(student + ": " + str(student_data[student]))

print("\n---------------------------------\n")

student = {
    "name": "Seth",
    "age": 16,
    "grade": "F"
}
print(student["name"] + " is " + str(student["age"]) + " years old.")

student["grade"] = "D+"

print("\n---------------------------------\n")

movie_data = {
    "Toy Story": "1994",
    "The Matrix": "1999",
    "Wall-E": "2008"
}
new_movie_name = input("What's the name of the movie you want to add?" \
"\n>> ")
new_movie_year = input("What year was it released?" \
"\n>> ")
movie_data[new_movie_name] = new_movie_year
print(movie_data)

print("\n---------------------------------\n")

fruit_data = {
    "pear": "$0.69",
    "apple": "$0.99",
    "cantaloupe": "$4.00"
}
frut_to_remove = input("What fruit should be removed?" \
"\n>> ")
try: 
    fruit_data.pop(frut_to_remove)
except:
    print("FAILED")
print(fruit_data)

print("\n---------------------------------\n")

words = ["cat", "rat", "bat", "cat", "cat", "cat", "cat", "dog", "rat"]
word_data = {}
for word in words:
    if word in word_data:
        word_data[word] += 1
    else:
        word_data[word] = 1
print(word_data)

print("\n---------------------------------\n")

employee_data = {
    "Seth": 5,
    "Silas": 10,
    "Chase": 80000,
    "Coooperr D.eee": 12000
}
highest_name = ""
highest_salary = 0
for employee in employee_data:
    if employee_data:
        continue