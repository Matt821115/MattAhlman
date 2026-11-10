for x in range(1,21,1):
    if x == 16:
        break
    print(x)

print("\n--------------------------\n")

for x in range(1,31,1):
    if x % 2:
        print(x)

print("\n--------------------------\n")

for x in range(1,21,1):
    if x == 16:
        pass # pass the save check
    print(x)

print("\n--------------------------\n")

for x in range(10,0,-1):
    if x == 5:
        continue
    print(x)

print("\n--------------------------\n")

list = [1,4,6,2,6,87,2,8,25,4,9,3,4,-5,5,-6,-2,6]
for x in list:
    if (x in list) < 0:
        break
    print(sum(list))

# fixed
sum = 0
for num in list:
    if num < 0:
        break
    sum += num
    print(sum)