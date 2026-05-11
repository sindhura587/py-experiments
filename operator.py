i = 1
j = not not i

print("j : ",j)

# loop through string and print name with a comma and new line
for c in "john.smith@pythoninstitute.org":
    print(c, end=",\n")
    if c == "@":
        print(" ch1 : ",c)
        break
    # print(c, end="")

print("\n*******************************************************")
print("Example : ","string splitting") 
test =""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
       break
    else:test += ch
print("test : ",test)

print("*******************************************************")
print("Example : ","If condition is true, then this part is executed.")
print("*******************************************************")

n = input("Enter plant name ")
if n=="Spathiphyllum" : print("Spathiphyllum is the best plant ever!")
elif n=="spathiphyllum" : print("No, I want a big Spathiphyllum!")
else : print("Spathiphyllum! Not "+ n +"!")

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
    if(year%4!=0 ): print(year," : common year :")
    elif(year%100!=0 ): print(year, " : Leap year")
    elif(year%400!=0 ): print(year, " : common year")
    else : print(year," : Leap year")
	

#loop
#while True:
 #   print("I'm stuck inside a loop.")

 # Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Enter a Integer : "))

while int(secret_number)!= number :
    print ("Ha ha! You're stuck in my loop!")
        
    number = int(input("Enter a Integer : "))
print("Well done, muggle! You are free now.")
       

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
for n in range(1,6):
    print(n," Mississippi")
time.sleep(1)
print("Ready or not, here I come!")
# Write a print function with the final message.


# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = (input("Enter a word : "))
user_word = user_word.upper()


for letter in user_word:
    # Complete the body of the for loop.
    if letter =="A": continue
    elif letter =="E": continue
    elif letter =="I": continue
    elif letter =="O": continue
    elif letter =="U": continue
    print(letter)

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height=nextlen=counter=1
while counter < blocks:
    
    nextlen += 1
    counter +=nextlen
    if counter <= blocks:
        height += 1
print("The height of the pyramid:", height)





