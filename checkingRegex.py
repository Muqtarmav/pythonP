import re
import re as regex
import bcrypt
import collections

Team = collections.namedtuple('details', [
    'name',
    'age',
    'country',
    'height',
    ]
)

details = Team(name='bola tinubu', age=33, country='Nigeria', height=7.3)
print(details)

print(details.name)
#

country = collections.namedtuple( 'state',  [

    'police',
    'electricity',
    'water',
                                  ])
result = country(police= 100, electricity= 'good', water= 'bad')

print(result.police)
# regex = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
#
# email = input("enter an email")
#
# def check(email):
#     if(re.search(regex, email)):
#          print("Valid Email")
#     else:
#          print("Invalid Email")
#
#
# print(check(email))
#
#
# password = b"ayomuqtar"
# hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#
#
# print(hashed)


List = [
    {'name': 'muqtar', 'age': 18, 'height': 6.9, 'country': 'dubai'},
    {'name': 'muqtar2', 'age': 18, 'height': 6.9, 'country': 'dubai'}
]


print(List[0]['name'])


List[1]['age'] = 22
print(List)

