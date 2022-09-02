## Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
counter  = 0
sum_of_lists = 0

for i in student_heights:
    sum_of_lists = sum_of_lists + i
    counter = counter + 1

height_average = sum_of_lists/counter
rounded_height = round(height_average)
print(rounded_height)

## Highest Scores

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
        #print(highest_score)

print(f"The highest score in the class is: {highest_score}")

##Adding Even Numbers

even = 0
for i in range(1, 101):
    if ( i % 2 == 0):
        #print(i)
        even = even + i
        #print(even)

print(even)

##FizzBuzz Game

for i in range(1, 101):
    if ( (i%5) == 0 ) and ( (i%3) == 0 ):
        print("FizzBuzz")
    elif (i%5) == 0:
        print("Buzz")
    elif (i%3) == 0:
        print("Fizz")
    else:
        print(i)
