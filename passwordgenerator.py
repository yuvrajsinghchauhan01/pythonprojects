#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []
#letters
for char in range(nr_letters):
    password_list.append(random.choice(letters))
#symbols
for sym in range(nr_symbols):
    password_list.append(random.choice(symbols))
#numbers
for num in range(nr_numbers):
    password_list.append(random.choice(numbers))

#1
# random_pass = ""
# random.shuffle(password_list)
# for char in password_list:
#     random_pass += char
# print(f"Your password is: {random_pass}")



#2
random_pass = ""
for _ in range(len(password_list)):
    random_pass += random.choice(password_list)
print(f"Your password from method 2 is: {random_pass}")



