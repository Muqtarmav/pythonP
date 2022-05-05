import math

result = math.sqrt(100)
print(result)


def rectangle_area(length=3, width=5):
    return length * width

print(rectangle_area())


def average(*args):
    return sum(args) / len(args)


print(average(10, 11, 34, 55))


stack = []

stack.append("green")
stack.append("blue")
stack.append("yellow")

print(stack)

stack.pop()
print(stack)


list1 = []

for items in range( 1, 6):
    list1.append(items)

print(list1)


counter = 0
total = 0

while counter <= 5:
    print(counter)
    counter = counter + 1


list = [1, 4, 6, 7, 8]
total = 0

for x in list:
    print(x)
    total = total + x
    print(total)

count = 1
while count < 10:
    print(count)
    if count == 8:
        break
    count = count + 1

#getting the arithmetic of 2 numbers
number1 = int(input("enter number 1 "))
print(number1)
number2 = int(input("enter number 2 "))
print(number2)
addition = number1 + number2
division = number1 / number2
multiply = number1 * number2
substraction = number1 - number2

print(addition)
print(division)
print(multiply)
print(substraction)

#comparing two numbers

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))

if number1 > number2:
    print(number1)
elif number1 == number2:
    print("these numbers are equal")
else:
    print(number2)


#computing three integers

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
number3 = int(input("enter third number"))


addition = number1 + number2 + number3
division = number1 / number2 / number3
multiply = number1 * number2 * number3
substraction = number1 - number2 - number3

print(addition)
print(division)
print(multiply)
print(substraction)


resultMin = min(number1, min(number2, number3))
resultMax = max(number1, max(number2, number3))

print(resultMin)
print(resultMax)




#check for even and odd
number = int(input("enter number "))

if number % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")


#check for multiples of two numbers
number1 = int(input("enter number 1 "))
number2 = int(input("enter number 2 "))

if number1 % number2 == 0:
    print("its a multiple")
else:
    print("not a multiple")

#RADIUS, DIAMETER OF A CIRCLE
radius = int(input("enter radius as a int"))

diameter = radius * radius

circum  = 2 * math.pi * radius

area = math.pi * radius * radius

print(diameter)
print(circum)
print(area)


#COUNT POSITIVE, NEGATIVE AND ZEROS

number1 = int(input("enter number 1"))
number2 = int(input("enter number 1"))
number3 = int(input("enter number 1"))
number4 = int(input("enter number 1"))
number5 = int(input("enter number 1"))

numPositive = 0
numNegative = 0
numZero = 0

if number1 > 0:
    numPositive = numPositive + 1
if number2 > 0:
    numPositive = numPositive + 1
if number3 > 0:
    numPositive = numPositive + 1
if number4 > 0:
    numPositive = numPositive + 1
if number5 > 0:
    numPositive = numPositive + 1

#negative

if number1 < 0:
    numNegative = numNegative + 1
if number2 < 0:
    numNegative = numNegative + 1
if number3 < 0:
    numNegative = numNegative + 1
if number4 < 0:
    numNegative = numNegative + 1
if number5 < 0:
    numNegative = numNegative + 1

#zero

if number1 == 0:
    numZero = numZero + 1
if number2 == 0:
    numZero = numZero + 1
if number3 == 0:
    numZero = numZero + 1
if number4 == 0:
    numZero = numZero + 1
if number5 == 0:
    numZero = numZero + 1


print(numPositive)
print(numNegative)
print(numZero)
#
# Chapter4
# finding the largest value

largestValue = 0
digits = 0
count = 0

while count < 10:
    digits =  int(input("enter numbers "))
    count = count + 1


    if digits > largestValue:
        largestValue = digits

print(largestValue)
#
# validating input

digit = int(input("enter number"))

while digit != 1 & digit != 2:
    digit = int(input("enter number "))




gallons = 0
mpg = 0.0
totalmpg = 0.0
totalMiles = 0
totalGallon = 0


miles = int(input("enter miles number or -1 to quit"))

if miles != -1:
    gallon = int(input("enter gallons"))

while miles != -1:
    totalMiles = miles + 1
    totalGallon = gallons + 1
    mpg = float (miles / gallons)
    totalmpg = totalMiles / totalGallon

    print(mpg)
    print(totalmpg)

    miles = int(input("enter miles or -1 to quit"))
    if miles != -1:
        gallon = int(input("enter gallon"))




# Hollow Square
count = 1
column = 1
while count <= 5:
    count = count + 1
while column >= 10:
    column = column +1
    if count == 1 | count == 5 | column == 1 | column == 10:
        print("*")
else:
    print(" ")

print()



# filledSQUARE

count = 0
column = 0

while count <= 5:
    count = count + 1
    if column == 0 & column <= 10:
        column = column + 1
    print("*")

print()

factorial

number = 5
factorial = 1
count = 1

while count < number:
    count = count + 1
    factorial = factorial * count
print("the factorial of", count, 'is ', factorial)


count integers

number = 74883993
count = 0


while number != 0:
    number = number / 10
    count = count + 1
print(count)


#Length of a string

word = "amazing"
count = 0
for i in word:
    count = count + 1
print(count)


#count vowels, consonant, digits, spaces

vowels = 0
consonant = 0
digit = 0
spaces = 0
count = 0

name = "Hello who is at home"
while count < len(name):
    print(name[count])
    if name[count] == "a" | name[count] == "z":
        consonant += 1
    count += 1

print(consonant)
