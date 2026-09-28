def greet():
    name = input("Your name is?\n>> ")
    print(f"Hello {name}!")

greet()

def add(x, y):
    print(x + y)
    return x + y

x = int(input("x="))
y = int(input("y="))

add(x, y)
test = add(9,11)
print(test)