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

