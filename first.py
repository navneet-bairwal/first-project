#!/usr/bin/env python3.6
##This project has been cloned to GIT
#first_name = "Navneet"
#Last_name = "Bairwal"
#age = 30
#birth_date = "08_09_1989"
#
#print(f"My name is: {first_name} {Last_name}")
#print(f"And my age is {age}")
#print(f"born on {birth_date}")
#
## Exercise2

users = [{'admin': True, 'active': True, 'name': 'Navneet' },
         {'admin': False, 'active': True, 'name': 'Nidhi' },
         {'admin': True, 'active': True, 'name': 'Lalit' }]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
