# Start by copying this code block into a new file called dataconversion.py in your unit 2 folder. This is an ungraded activity.

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = int(115)           #int -> string
b = float(3.14)        #float -> string
c = "68"               #string -> int
d = "True"             #string -> boolean
e = True               #boolean -> string
f = False              #boolean -> string
g = '10110111'         #byte -> int
h = "2.54"             #string -> float
i = int(100)           #int -> float
j = float(10.0)        #float -> int
k = int(254)           #int -> byte

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

a = str(a)
b = str(b)
c = int(c)
d = bool(d)
e = str(e)
f = str(f)
g = int(g)
h = float(h)
i = float(i)
j = int(j)
k = bytes(k)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)