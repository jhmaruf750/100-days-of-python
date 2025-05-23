import string
import random

# All lowercase and uppercase letters
letters = list(string.ascii_letters)  # ['a' to 'z' and 'A' to 'Z']

# All digits (0-9)
numbers = list(string.digits)  # ['0' to '9']

# All symbols (common punctuation)
symbols = list(string.punctuation)  # ['!', '"', '#', '$', '%', '&', etc.]



print("welcome to the pypassword Generator!")

cnt_letters=int(input("How many letters would you like in your password?\n"))
cnt_symbols=int(input("HOw many symbols would you like?\n"))
cnt_numbers=int(input("HOw many numbers would you like?\n"))


#Easy level

password=""

for char in range(0,cnt_letters):
    password+=random.choice(letters)

for char in range(0,cnt_symbols):
    password+=random.choice(symbols)

for char in range(0,cnt_numbers):
    password+=random.choice(numbers)

print(password)


#hard level

password_list=[]

for char in range(0,cnt_letters):
    password_list.append(random.choice(letters))

for char in range(0,cnt_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,cnt_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

passw= ""

for char in password_list:
    passw+=char

print(passw)




