# 100daysofPython - Day 4

Day 4 is all about introduction of Lists and using the Random module.

For randomness, python uses a logic called "Mersenne Twister."

There's a Udemy Course for this logical called Pseudorandom number generators.

Some of methods presented

random.ranint(start, stop)  >> generates a random number from given start range, end range
random.seed >> used in checking the problem sets, this will result in a same output when reprogram
random.random() >> used for generating numbers out of floating values, range here is 0.0 to 0.9 but you can mulitply to an integer to have a whole number and a decimal

Lists - enclosed in [] and are immutable.

Changing the value of a list is through indeces and equal sign, fruits[0] = "blueberries"

Using .append() to insert one value at a time
Using .extend() for adding a list to a list

fruits = ["apple", "banana"]
fruits.extend( ["mangoes", "strawberries"] )
print(fruits)

Output: ['apple', 'banana', 'mangoes', 'strawberries']

>> len() as a way to count elements in a list
>> how to access nested list
>> how a 3x3 matrix can be represented as a a list: this is a hard exercise named "Treasure Map"

>> using random and lists to generate a game called rock, papers, scissors

Exercises: 
1) Heads or Tails - using randint function, 1 will be set to Heads and 0 as Tails
2) Banker Roulette - code uses a randint to determine who will pay the bill out of the number of names presented
3) Treasure Map - this is pretty complicated since lists are use to perform like matrix, basically the concept is it will put an 'X' when a you give a 2-digit value. Here is a sample.

![image](https://user-images.githubusercontent.com/107990192/188195352-8808e53e-fa09-4991-abf6-bf35bbe1176a.png)

The analogy here would be the last digit would be used as a row to get inside the list and the first digit is a column to get inside of the list we accessed from row.

Project: 
Rock Paper Scissors - with ASCII characters of rock, paper and scissors computer would use a randint to choose between a rock, paper and scissor versus the user's choices. Instead of printing the result as a word, it will be produced as an image.
