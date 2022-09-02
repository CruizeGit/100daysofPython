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

for_letters = []
for_numbers = []
for_symbols = []

for l in range(nr_letters):
  x = random.randint(0, len(letters)-1)
  letters_char = letters[x]
  for_letters.append(letters_char)

#print(for_letters)
string_let = ''
for i in for_letters:
  #print(i)
  string_let = string_let + i

#print(string_let)

for n in range(nr_numbers):
  x = random.randint(0, len(numbers)-1)
  numbers_char = numbers[x]
  for_numbers.append(numbers_char)

#print(for_numbers)

string_num = ''
for i in for_numbers:
  string_num = string_num + i

#print(string_num)
  
for s in range(nr_symbols):
  x = random.randint(0, len(symbols)-1)
  symbols_char = symbols[x]
  for_symbols.append(symbols_char)

#print(for_symbols)

string_sym = ''
for i in for_symbols:
  string_sym = string_sym + i

#print(string_sym)

easy_password = string_let + string_num + string_sym
print(f"Here's your password: {easy_password}")

