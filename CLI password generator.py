import random
import string

try:
    length = int(input("Enter password length :"))
except ValueError:
    print("Please enter a valid number")
    exit()

mandatory = 3

if length < mandatory:
        print("Password length should be at least", mandatory)
        exit()

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

upp = random.choice(string.ascii_uppercase)

digit = random.choice(string.digits)

sym = random.choice(string.punctuation)

password = upp + digit + sym

for i in range(length - mandatory):
    
    random_char = random.choice(characters)
    password = password + random_char

pass_list = list(password)

random.shuffle(pass_list)

password = "".join(pass_list)

print("password :", password)


