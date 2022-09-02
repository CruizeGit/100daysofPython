import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


##nrs is used as a placeholder for the user's number of list
nrs = [nr_letters, nr_symbols, nr_numbers]

print(nrs)
 
pwd = ''
 
while nrs[0] != 0 or nrs[1] != 0 or nrs[2] != 0:  #will keep on looping as long as the number of preferred char is not satisfied
  
    char_type = random.randint(0, 2)
 
    if char_type == 0 and nrs[0] != 0: # random letter
#         pwd += letters[random.randint(0, len(letters)-1)]
          pwd = pwd + letters[random.randint(0, len(letters)-1)]            ##this will get random elements in letters
#         nrs[0] -= 1
          nrs[0] = nrs[0] - 1  #will basically deduct the number of letters on each iteration, this will satisfy the required number of letters
 
    elif char_type == 1 and nrs[1] != 0: # random number
#         pwd += numbers[random.randint(0, len(numbers)-1)]
          pwd = pwd + numbers[random.randint(0, len(numbers)-1)]
#         nrs[1] -= 1
          nrs[1] = nrs[1] - 1 #will basically deduct the number of numbers on each iteration, this will satisfy the required number of letters
          
 
    elif char_type == 2 and nrs[2] != 0: # random symbol
#         pwd += symbols[random.randint(0, len(symbols)-1)]
          pwd = pwd + symbols[random.randint(0, len(symbols)-1)]
#         nrs[2] -= 1
          nrs[2] = nrs[2] - 1 #will basically deduct the number of numbers on each iteration, this will satisfy the required number of letters
 
print(pwd)