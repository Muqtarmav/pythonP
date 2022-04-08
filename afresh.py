import datetime
import random

value = 2 + 3
print(value)

answer = 3 > 2
print(answer)

word = "hello world"
print(word)

'''
ignore this line my friend
'''

userAge, userName = 30, "ade"

print(userAge)
print(userName)

x = 6
y = 10
x = y

print(x)
print(y)


x = 5
t = 8

print(x + t)
print(x / t)
print(x // t)
print(x % t)

x = x + 2
print(x)

message = 'what is my name :  %s if its correct what is my age : %d' %('muqtar', 22)
print(message)

message = 'can you tell me {} you make your {}'.format('how', 'money')
print(message)

print(ord("c"))

A = int("4")
print(A)

B = str("3333")
print(B)

print(str(datetime.datetime.now().date()))


A = 77
b = 66

if(A > b):
    print("correct")


fruits = ["apple", "banana", "orange"]
x, y, z = fruits
print(x)
print(y)


x = "awesome"

def myfunc():
    print("python is "  + x)

myfunc()


y = "muqtar"


def myFunc():
    y = "ade"
    print("this is my name " + y)

myFunc()

print(y)


#Numeric types

x = 5
y = "hello"
z = 42j

print(type(x))
print(type(z))

print(z)

c = float(x)
d = complex(x)
print(c)
print(d)

print(random.randrange(1, 10))

#loop through string
name = "Muqtar"

for x in name:
    print(x)

print(len(" this is the length of string " + name))

for j in "banana":
    print(j)


b = "hello word"

if ( "hello" in b):
    print("true")


animal = "leopard"

print(animal[1:5])

print(animal.replace("l", "m"))
print(animal.upper())


#List

name = ["tola", "fola",]

name[1] = "fhona"
(name.insert(3, "shola"))
print(name)


letters = ['a', 'd' 'gf']
numb = [1, 2, 5, 6]

letters.extend(numb)
print(letters)


name = ["bola", "tola", "segun"]
print(name.insert(3, "bimpe"))
print(len(name))

print(name)

age = [11, 15, 16, 18]
name.extend(age)

print(name)


cities = ["london", "lagos", "abia", "kogi"]

cities.remove("abia")

cities.pop()
print(cities)


