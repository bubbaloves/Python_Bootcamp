#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# passwd = ""
# for letter in range(1,nr_letters+1):
#     pw_let = random.choice(letters)
#     passwd = passwd + pw_let
# for symbol in range(1,nr_symbols+1):
#     pw_sym = random.choice(symbols)
#     passwd = passwd + pw_sym
# for number in range(1,nr_numbers+1):
#     pw_num = random.choice(numbers)
#     passwd = passwd + pw_num

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Obtain amount of characters
passwd_char_list = []
for letter in range(1,nr_letters+1):
    pw_let = random.choice(letters)
    passwd_char_list.append(pw_let)
for symbol in range(1,nr_symbols+1):
    pw_sym = random.choice(symbols)
    passwd_char_list.append(pw_sym)
for number in range(1,nr_numbers+1):
    pw_num = random.choice(numbers)
    passwd_char_list.append(pw_num)

#shuffle set of obtained random characters
random.shuffle(passwd_char_list)

#obtain characters from list and print as string
passwd = ""
for n in range(0, len(passwd_char_list)):
    passwd = passwd + passwd_char_list[n]

#print random password string
print(passwd)

