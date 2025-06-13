
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# result = len(name) #function that tells you how many chars(LENGHT)
# result = name.find("a") the first A
# result = name.rfind("a") the last A
# name = name.capitalize() FIRST UPPERCASE LETTER
# name = name.upper() ALL CAPS
# name = name.lower() ALL LOWERCASE
# result = name.isdigit() TRUE OR FALSE(TRUE IF ONLY NUMBERS)
# result = name.isalpha() TRUE IF THERE IS NO SPACE OR NUMBERS
# result = phone_number.count("-") COUNT HOW MANY -(ANYTHING) THERE ARE
# phone_number = phone_number.replace("-", " ") TO REPLACE

# print(phone_number)

# print(help(str)) FUNCTIONS LIKE THE ABOVE


# validate user input exercise
# 1.username is no more than 12 characters
# 2.username must not contain spaces
# 3.username must not contain spaces

name = input("Enter your username: ")
space = name.isalpha()
if len(name) >=12:
    print("Your username can't be more than 12 characters")
elif not name.find(" ") == -1:
    print("Your username can't contain spaces")
elif not name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {name}")