x = 1
a = float(x)

print(a)

b = complex(x)
print(b)


#Strings

a = "Hello world"

print(len(a))

print(a[2:7])


b = "welcome"

print(b.upper())

print(b.replace("w", "r"))

a = "hello"
b = "world"

c = a + " " +  b
print(c)

List = ["orange", "apple", "guava"]

print(len(List))


for y in List:
    print(y)

    #List of different types

newlIST = ["ayo", 44, 3.2, True]

print(newlIST[1])

if "boss" in newlIST:
    print("yes boss is present")
else:
    print("boss is not present")


    #insert an element in a list

myList = ["apple", "basket", "curry"]

myList.insert(3, "goat")

print(myList)

aList = ["rice", "beans", "garri"]

aList.append("dodo")
aList.extend(myList)
print(aList)


bList = ["cat", "dog", "snake", "lion"]

bList.remove("snake")
print(bList)


cList = ["cat", "dog", "snake", "lion"]
cList.pop(1)

print(cList)


dList = ["lagos", "Edo", "Kano", "Kogi", "Kwara"]
eList = []

for x in dList:
    if "a" in x:
        eList.append(x)

    print(eList)


