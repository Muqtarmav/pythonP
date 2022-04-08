# userInput = input("enter 1 or 2")
#
#
# if userInput == "1":
#     print("you are doing well")
#     print("you are amazing")
# elif userInput == "2":
#     print("you got this")


#range
#
# for numbers in range(10):
#     print(numbers)


number = 3
total = 0

while number <= 50:
    number = number * 3
print(number)
#
# total = total + number
# print(total)
#
# digit = 2
# total = 0
#
# while digit < 10:
#     digit = digit + 1
#     total = total + digit
# print(digit)
#
#
# print( total)
#
#
# new_total = 0
# grade_counter = 0
#
# grades = [10, 11, 23, 14, 55, 23, 45, 44, 76, 46]
#
# for b in grades:
#     grade_counter = grade_counter + 1
#     total = total + b
#     average = total / 10
#
# print("here is the average %d", average)
# print(total)
#
#
# #sentinel value
# total = 0
# counter = 0
#
# grade = int(input("enter grade or -1 to quit"))
#
# while grade != -1:
#     counter = counter + 1
#     total = total + grade
#     grade = int(input("enter grade or -1 "))
#
# average = total / 10
# print(total)
# print(average)

# for number in range(2, 101, 2):
#     print(number)


def func(number):
    return number * 2

print(func(7))

print(func(2.5))


def maximum(number1, number2, number3):
    maximum = number1
    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    return maximum

print(maximum(1111, 555, 55))

list = ["ade", "segun", "fola", "doma"];
print(list[1:3])


country = "amaerica"

print(country)
for x in country:
    print(x)

digit = [1, 3, 5, 7, 9]
digit.append(11)
digit.insert(2, 10)
digit.remove(3)
print(digit)


list.extend(digit)
print(list)

#loop through index number
thisList = ["apple", "banana", "orange", "kiwi", "melon"]
aLIST = []

for x in thisList:
    if "a" in x:
        aLIST.append(x)

print(aLIST)



numerals = [11, 2, 4, 55, 6, 3, 4]

numerals.sort(reverse=True)
print(numerals)


cities = ["london", "dubai", "Togo", "NewYork"]

cities.sort(key=str.lower)
print(cities)

age = [1, 4, 6]
currency = ["naira", "cedis", "pounds"]

list3 = age + currency
print(list3)

#tuple

thisTuple = ("ball", "cat", "lion", "cat", "rat")
print(thisTuple)

tuple = ("beans",)
print(tuple)

#add item into tuples

newT = ("game", "dance", "laugh")

for f in newT:
    print(f)


#SET

set = {"apple", "banana", "guava", "apple"}
set.add("cake")
print(set)

setB = {1, 3, 5, 6}
result = set.union(setB)
print(result)

A = {"ade", "bola", "ola"}

B = {"tinu", "ola"}

A.intersection_update(B)
print(A)

# A.intersection(B)
# print(A)

Y = {"ade", "bola", "ola"}

Z = {"tinu", "ola"}

Y.symmetric_difference(Z)
print(Z)