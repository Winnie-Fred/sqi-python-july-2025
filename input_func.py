# Ask the user for their age and tell them what year they were born


# from datetime import datetime
# import datetime

# PSL -> Python Standard Library

# age = input("How old are you now? ")
# # future-proofing
# # current_year = datetime.today().year
# current_year = datetime.datetime.today().year
# print(current_year)

# birth_year = current_year - int(age)
# print(f"You were born in {birth_year}")


# blind-typing

# from getpass import getpass

# password = getpass("Enter your password: ")
# print(f"Your password is: {password}")


# age = 12
# name = "Olaitan"

# age = input("How old are you now? ")
# print(f"You are {age} years old")

# name = input("Enter your name: ")
# print(f"Your name is {name}")


# Ask the user to enter their favorite color
# Then print "{fav_color} is awesome".


# Ask the user for their age
# Then tell them when they were born
# You were born in {birth_year}

# from datetime import datetime

# current_year = datetime.now().year

# age = int(input("How old are you now? "))
# birth_year = current_year - age
# print(f"You were born in {birth_year}")


# Ask the user for 2 numbers, num1 and num2
# Then tell them the sum of the numbers

# Sample Execution
# Enter the first number: 5
# Enter the second number: 6
# The sum of 5 and 6 is 11


# Enter the first number: 15
# Enter the second number: 4
# The sum of 15 and 4 is 19

# first_num = input("Enter the first number: ")
# second_num = input("Enter the second number: ")
# sum_of_nums = int(first_num) + int(second_num)

# print(f"The sum of {first_num} and {second_num} is {sum_of_nums}")
# print("The sum of " + first_num + "and " + second_num + " is " + str(sum_of_nums))



# Sample Execution
# Enter a three-digit number: 453
# The sum of the digits is 12

# Enter a three-digit number: 208
# The sum of the digits is 10

# digits = input("Enter a three-digit number: ")
# print(f"The sum of the digits is {int(digits[0]) + int(digits[1]) + int(digits[2])}")

# + - polymorphic


# sum_of_nums = sum([7, 8, 9])
# print(sum_of_nums)

# name = "Daniel"
# name_upper = name.upper()
# print(name_upper)

# name = "Daniel"
# no_of_a = name.count('a')
# print(no_of_a)

# method is a function inside a class




# ASSIGNMENT CORRECTION
# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

# name = input("What is your name? ").strip()
# print(f"Hello, {name}!")


# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

# from datetime import datetime


# birth_year = int(input("What year were you born? "))
# current_year = datetime.now().year
# age = current_year - birth_year
# print(f"You are {age} years old.")


# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.

# favorite_color = input("What is your favorite color? ").strip()
# print(f"Your favorite color is {favorite_color}.")


# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

# text = input("Enter some text: ").strip()
# is_palindrome = text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "")
# print("original text:", text)
# print("reversed text:", text[::-1])
# print(f"It is {is_palindrome} that {text} is a palindrome.")


# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

# from getpass import getpass

# password = getpass("Enter the password: ")
# # is_valid = len(password) >= 8 and len(password) <= 30
# is_valid = 8 <= len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria.")

# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# weight = float(input("Enter your weight (in kg): "))
# height = float(input("Enter your height (in metres): "))
# bmi = weight / (height ** 2)
# bmi = round(bmi, 2)
# print(f"Your BMI is {bmi}")


# verb = "dance"
# # verb[0] = "b"  #  wrong
# verb = verb.replace("d", "b")
# print(verb)


# text = ["Hello", "World"]
# print(text)
# print(type(text))