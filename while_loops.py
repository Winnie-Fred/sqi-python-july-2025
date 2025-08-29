# i = 1

# while i <= 10:
#     print(i, "Hi, good morning")
#     i += 1

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# 1. Write a loop that prints all the numbers between 78 and 105 (105 is included)

# i = 78

# while i <= 105:
#     i += 1
#     print(i)

# 2. Write a loop that prints only the even numbers between 7 and 89 i.e 8, 10, 12...86, 88

# i = 8

# while i < 89:
#     print(i)
#     i += 2

# 3. Write a loop that prints all the multiples of 3 between 2 and 50 i.e. do not set your i=3

# i = 2

# while i < 50:
#     print(i + 1)
#     i += 3


# i = 1

# while i < 50:
#     if i % 3 == 0:
#         print(i)
#     i += 1


# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")
# print("Hi, good morning")


# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(str(i))
#     i += 1

# print(numbers)
# print(", ".join(numbers))


# OR


# numbers = ""
# i = 1
# while i <= 50:
#     numbers += str(i)
#     if i != 50:
#         numbers += ", "
#     i += 1

# print(numbers)


# Print all the numbers from 1 to 50, separated by commas
# 1, 2, 3, 4, ..., 47, 48, 49, 50





# i = 1

# while i <= 50:
#     print(i)
#     i += 1


# i = 100

# while i < 8:  # never runs
#     print(i)
#     i += 1


# i = 1
# while i <= 40:
#     print(i)
#     if i == 20:
#         break
#     i += 1

# print("This will run")


# Print numbers from 6 to 20, but break once you come across a multiple of 10
# 6, 7, 8, 9

# i = 6

# while i <= 20:
#     if i % 10 == 0:
#         break
#     print(i)
#     i += 1

# 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19


# i = 0
# while i < 20:
#     i += 1
#     if i % 5 == 0:
#         continue
#     print(i)


# i = 1
# i = 100
# while i <= 40:
#     print(i)
#     if i == 20:
#         break
#     i += 1
# else:
#     print("Loop has ended")

# ABC

# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# number = int(input("Enter a number: "))

# i = 0

# while i < number:
#     print("*" * number)
#     i += 1


# Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111

# number = 10
# ones = ""

# i = 0
# while i < 10:
#     ones += "1"
#     i += 1

# print(ones)


# number = 10
# ones = []

# i = 0
# while i < 10:
#     ones.append("1")
#     i += 1

# print("".join(ones))


# 1. Learn how to loop through collections

# name = "Daniel"
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
# # print(name[5])


# name = "Daniel"
# i = 0

# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1



# Ask the user to enter a sentence, and loop through and print each character.
# Print only the characters at odd positions

# 2. Learn while True

# items = ["bag", "clothes", "cup", "shoe"]

# i = 0

# while i < len(items):
#     print(items[i])
#     i += 1


# story = []

# while True:
#     line = input("Enter a line of the story: ").strip()
#     if line.lower() == "stop":
#         break
#     story.append(line)


# story = "\n".join(story)
# print(story)

# story = []
# line = ""
# while line != "stop":
#     line = input("Enter a line of the story: ").strip()
#     if line.lower() == "stop":
#         break
#     story.append(line)


# story = "\n".join(story)
# print(story)



# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# balance = int(input("Enter your balance: "))
# while True:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt > balance:
#         print("Insufficient funds")
#         continue

#     balance -= withdrawal_amt
#     print(f"Remaning balance: {balance}")   

#     another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#     if another_withdrawal != "yes":
#         print(f"Final balance: {balance}")
#         break


# balance = int(input("Enter your balance: "))
# withdrawal_status = True
# while withdrawal_status:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt > balance:
#         print("Insufficient funds")
#         continue

#     balance -= withdrawal_amt
#     print(f"Remaning balance: {balance}")   

#     while True:
#         another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#         if another_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             withdrawal_status = False
#             break

#         if another_withdrawal == "yes":
#             break

#         print("Invalid response")



# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# Organization
# o - 2
# r - 1
# g - 1

# occurences = {}

# text = input("Enter some text: ").strip().lower()

# i = 0

# while i < len(text):
#     char = text[i]
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     i += 1
# print(occurences)

# # print(dict(sorted(occurences.items(), key=lambda item: item[1], reverse=True)))

# def get_dict_value(item):
#     _, value = item
#     return value

# print(dict(sorted(occurences.items(), key=get_dict_value, reverse=True)))

 

# ==================================ASSIGNMENT CORRECTION==================================
# While Loop Exercises 1
# 5. Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# i = 1

# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1



# 7. Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****

# triangle_base = int(input("Enter the length of the triangle base: "))


# i = 1

# while i <= triangle_base:
#     print("*" * i)
#     i += 1


# 10. Print a list of the first 12 multiples of 3 starting from 3
# first_12_multiples_of_3 = []

# i = 3
# while True:
#     if len(first_12_multiples_of_3) == 12:
#         break
#     first_12_multiples_of_3.append(i)
#     i += 3

# print(first_12_multiples_of_3)


# first_12_multiples_of_3 = []

# i = 3

# while len(first_12_multiples_of_3) != 12:
#     first_12_multiples_of_3.append(i)
#     i += 3

# print(first_12_multiples_of_3)

# While Loop Exercises 2
# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# total = 0
# numbers_up_to_n = []

# n = int(input("Enter a number: "))

# i = 1

# while i <= n:
#     total += i
#     numbers_up_to_n.append(str(i))
#     i += 1

# final_result = " + ".join(numbers_up_to_n)
# final_result += " = " + str(total)
# print(final_result)


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# import random

# secret_num = random.randint(1, 50)

# attempts = 5

# while attempts >= 1:
#     guess = int(input("Guess the secret number: "))

#     if guess > 50 or guess < 1:
#         print("The number must be between 1 and 50.")
#         continue

#     if guess == secret_num:
#         print("Congratulations 🥳. You guessed the secret number correctly")
#         break

#     if guess > secret_num:
#         print("You guessed too high.")
#     else:
#         print("You guessed too low")

#     attempts -= 1
#     print(f"You have {attempts} attempts left.")

# else:
#     print(f"You lost 😔. You ran out of attempts. The secret number was {secret_num}")

# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# while True:
#     password = input("Enter the password: ").strip()
#     if password == "secret":
#         print("Correct password")
#         break

#     print("Incorrect password")


# OR

# password = ""
# while password != 'secret':
#     password = input("Enter the password: ").strip()
#     if password != 'secret':
#         print("Invalid password")
# else:
#     print("Correct Password")


# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625


# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# i = exponent
# result = 1

# while i >= 1:
#     print(f"result = {result} * {base} = {result * base}")
#     result *= base
#     i -= 1

# print(f"{base} raised to the power of {exponent} is {result}")

# DRY - Don't Repeat Yourself

# 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# text = input("Enter some text: ").strip()
# vowels = "aeiouAEIOU"

# # food

# # 1. Check each character if it is a vowel
# # 2. If it is not a vowel, ignore it
# # 3. Else, count it


# i = 0
# no_of_vowels = 0


# while i < len(text):
#     char = text[i]

#     if char in vowels:
#         no_of_vowels += 1
    
#     i += 1

# print(F"Number of vowels: {no_of_vowels}")


# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

# sugar
# 01234

# ragus
# 43210

# text = input("Enter some text: ").strip()
# reversed_text = ""
# i = len(text) - 1

# while i >= 0:
#     char = text[i]
#     reversed_text += char
#     i -= 1


# print(reversed_text)

# sugar
# ragus

# text = input("Enter some text: ").strip()
# reversed_text = ""

# i = 0

# while i < len(text):
#     char = text[i]
#     reversed_text = char + reversed_text
#     i += 1

# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.

# numbers = tuple(input("Enter numbers separated by commas: ").split(","))

# smallest = int(numbers[0])

# i = 1

# while i < len(numbers):
#     num = int(numbers[i])
#     if num < smallest:
#         smallest = num
#     i += 1

# print(f"The smallest number is {smallest}")


# Even more while loop exercises

# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


# Version 1.0
# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam": 2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation == "add":
#         item = input("Enter item: ").strip().lower()
#         quantity = int(input("Enter quantity: "))
#         inventory[item] += quantity
#         print(f"Current inventory: {inventory}")
#     elif operation == "remove":
#         item = input("Enter item: ").strip().lower()
#         quantity = int(input("Enter quantity: "))
#         inventory[item] -= quantity
#         print(f"Current inventory: {inventory}")
#     elif operation == "exit":
#         break
#     else:
#         print("Invalid operation")



# Version 1.1
# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam": 2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation == "exit":
#         break

#     if operation not in ["add", "remove"]:
#         print('Invalid operation')
#         continue


#     item = input("Enter item: ").strip().lower()
#     quantity = int(input("Enter quantity: "))


#     if operation == "add":
#         if item in inventory:
#             inventory[item] += quantity
#             # inventory[item] = inventory.get(item, 0) + quantity
#         else:
#             inventory[item] = quantity
#     elif operation == "remove":
#         if item in inventory:
#             inventory[item] -= quantity
#         else:
#             print(f"{item} not in inventory")
    # print(f"Current inventory: {inventory}")


# ==================================ASSIGNMENT CORRECTION==================================




# ==============school
# |
# |
# |
# 5m
# |
# |
# |
# ==============bank
# |
# |
# 3m
# |
# |
# ==============mosque
# |
# 2m
# |
# ==============airport