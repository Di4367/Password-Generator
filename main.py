import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to my Password Generator!")
n_letters = int(input("How many letters would you like in your password? \n"))
n_symbols = int(input("How many symbols would you like? \n"))
n_numbers = int(input("How many letters would you like? \n"))

password_list = []
for char in range(1, n_letters+1):
    password_list += random.choice(letters)

for char in range(1, n_symbols+1):
    password_list += random.choice(symbols)

for char in range(1, n_numbers+1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password +=char

print(f"Your password is {password}")

