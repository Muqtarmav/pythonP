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


name = ["ade tola", "tola kola", "adigun"]
new_name = []

for i in name:
    new_name.append(i.upper().replace(" ", "_"))
print(new_name)


for num in range(1, 10, 2):
     print(num)

cities = ["kwara", "lagos", "kano", "benin"]

for w in range(len(cities)):
    print(w)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for dig in tokens:
    print(dig)
    if dig.count("<"):
        count = count + 1

print(count)

#modify name with range
name = ["ade tola", "tola kola", "adigun"]

for i in range(len(name)):
    name[i].lower().replace(" ", "_")
print(name)


#iterate thru dictionaries

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for n in cast.items():
    print(n)

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)

#
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count = 0
sum = 0
for numbers in num_list:
    if numbers % 2 != 0:
        count = count + 1

while count <= 5:
    sum = sum + numbers

    #print(numbers)
    sum = sum + numbers
print("sum of odd numbers", sum)


letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

word = ["boy", "girl", "male"]
digits = [1, 3, 4]

for word, digits in zip(word, digits):
    print(word, digits)