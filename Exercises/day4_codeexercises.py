#Exercise 4.1 - Heads or Tails
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
test_number = random.randint(0,1)

if test_number == 1:
    print("Heads")
else:
    print("Tails")


# #Exercise 4.2 - Banker Roulette
# import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_of_names= len(names)-1
get_random_number = random.randint(0, count_of_names)

lucky_winner = names[get_random_number]
print(f"{lucky_winner} is going to buy the meal today!")

#Exercise 4.3 - Treasure Map

#nested lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
# veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, veggies]
# print(dirty_dozen)

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_column = int(position[0])-1
position_row = int(position[1])-1


##THINK OF IT AS A LIST
##ANG ANALYSIS NENTO IS UNG SA MAP, INALAYZE MO SIYA BILING LIST, UNG 32 KUNYARI 2 WOULD ACTUALLY BE THE ROW
##3 IS A WAY PARA MAACESS UNG COLUMN OR PARA MAGING DUUN SIYA SA LIST
# print(map)
# print(position_column, position_row)
# positioning = map[position_row][position_column]
#[row1, row2, row3][position_row][position_column] = 'X'
map[position_row][position_column] = 'X'
# print(positioning)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

