import re
def check_name():
    name_pattern=r'[A-Za-z]'
    name=input("Enter your name: ")
    if name[0].isupper() and name[1:].islower() and re.match(name_pattern,name):
        return 1,name
    else:
        return 0,"not_accepted"

def check_surname():
    surnamename_pattern=r'[A-Za-z]'
    surname=input("Enter your surname: ")
    if surname[0].isupper() and surname[1:].islower() and re.match(surnamename_pattern,surname):
        return 1,surname
    else:
        return 0,"not_accepted"

def check_phone():
    phone_pattern = r"\(\d{2}\)\d{3}-\d{2}-\d{2}"
    phone=input("Enter your phone numer, in format (99)999-99-99: ")
    if re.match(phone_pattern,phone):
        return 1, phone
    else:
        return 0,"not_accepted"

def check_code():
    code_pattern = r"\d{2}\-\d{3}"
    code=input("Enter your post code in format 99-999: ")
    if re.match(code_pattern,code):
        return 1,code
    else:
        return 0,"not_accepted"

def check_town():
    town = input("Enter your town name: ")
    town_pattern=r'[A-Za-z]'
    if town[0].isupper and town[1:].islower and re.match(town_pattern,town):
        return 1,town
    else:
        return 0, "not_accepted"

n, name = check_name()
while 1:
    while n!=1:
        n, name = check_name()
    s,surname=check_surname()
    while s!=1:
        s,surname=check_surname()
    p,phone=check_phone()
    while p!=1:
        p,phone=check_phone()
    c,code=check_code()
    while c!=1:
        c,code = check_code()
    t,town=check_town()
    while t!=1:
        t,town=check_town()
    break

print("Data correct: ")
print(name,surname,phone,code,town)