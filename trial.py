for i in range(3):
    print("hello")

for digit in range(1, 10, 2):
    print(digit)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
names = []

for name in usernames:
    names.append(name.lower().replace(" ", "_"))

print(names)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in range(len(usernames)):
    usernames[name] = usernames[name].lower().replace(" ", "_")

print(usernames)

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for objects, count in basket_items.items():
   if objects in fruits:
    fruit_count += count
else:
    not_fruit_count += count

print("total number of fruit is {}".format(fruit_count, not_fruit_count))
