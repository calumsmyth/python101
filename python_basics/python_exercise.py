#If Statement
#Exercise 1 - Check if number is even
num = 8
if num % 2 == 0:
    print("The number is even")


#Exercise 2 - Display a message if a list is empty
list = []
if len(list) == 0:
    print("List is empty")




#else Statement
#Exercise 1 - Is number odd or even
num = 4
if num % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")




#elif statement
#Exercise 1 - Write a script for Temp categories
temp = 30
if temp <=0:
    print("IT's freezing!")
elif temp <= 10:
    print("It's cold")
elif temp <= 20:
    print("It's about normal")
elif temp <= 25:
    print("It's warm today")
else:
    print("It's very hot!")




#Loop
#Exercise 1 print each character in a string
string = "Hello, world."
for letter in string:
    print(letter)



#While Loop
#Exercise 1 - Add numbers until sum reaches 100

total_sum = 0
current_number = 1
while total_sum < 100:
    total_sum += current_number
    current_number +=1

print("The total sum of numbers until reaching 100 is", total_sum)



#Infinite Loops and break - Completed in lesson and experimented with Code to make a game which suggests whether unknown number is higher or lower than guess.
#Also revealed answer if 3 incorrect guesses. 