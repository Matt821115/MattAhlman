def mult():
    num = input("Enter a number\n>> ")
    num_two = input("Enter another number\n>> ")
    try:
        print(float(num) * float(num_two))
    except:
        print("INVALID INPUT")
        mult()
mult()
print("Finished")