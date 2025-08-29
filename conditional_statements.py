# is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Enjoy the sunshine")


# num1 = 100
# num2 = 100

# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 == num2:
#     print("num1 and num2 are equal")
# else:
#     print("num1 is less than or equal to num2")


# print("this will run regardless")



# 1. Define the following variable
# num = 10
# # Print "9 is even" if num is even, else, print "9 is odd" if it is not even

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


# 2. Define the following variable
# name = "Ola"
# # if name.endswith("a"):
# if name[-1] == "a":
#     print("It ends with a")
# else:
    # print("it doesn't end with a")
# Print "It ends with a" if name ends with "a", otherwise, print "it doesn't end with a"

# 3. Define the following variable
# score = -5
# if 0 <= score < 30:
#     print("Fail")
# # elif score >= 30 and score < 50:
# elif 30 <= score < 50:
#     print("Pass")
# elif score >= 50:
#     print("Well done")
# else:
#     print("Invalid score")





# If the person either has an umbrella or has a raincoat, print "You are protected from the rain"
# Else, if the person has both an umbrella and a raincoat, print "You are WELL protected from the rain"
# Otherwise, if they have neither, print "You are NOT protected from the rain."

# has_raincoat = True
# has_umbrella = True

# if has_raincoat and has_umbrella:
#     print("You are well protected from the rain")
# elif has_raincoat or has_umbrella:
#     print("You are protected from the rain")
# else:
#     print("You are not protected from the rain")


# import string

# alphabets = string.ascii_letters

# name = input("Enter your name: ").strip()


# # if name != "":
# if name:
#     if name.isalpha():
#         print(f"Hello, {name}")
#     else:
#         print("Invalid name entered. Name must contain only letters.")
# else:
#     print("Hello, Anonymous")

# names = ["Winnie", "James", "Ella"]
# # print(str(names)[1])  # wrong
# print(", ".join(names))



# OR


# import string

# alphabets = string.ascii_letters

# name = input("Enter your name: ").strip()

# if not name:
#     print("Name must not be blank")
# else:
#     if set(name).issubset(set(alphabets)):
#         print(f"Hello, {name}")
#     else:
#         print("Hello, Anonymous")


# names = []
# # If names is empty, print "No one to greet"
# # otherwise if name is not empty e.g:
# # names = ["Winnie", "James", "Ella"]
# # print("Hello, Winnie, James, Ella")

# if not names:
#     print("no one to greet")
# else:
#     print(f"Hello, {", ".join(names)}")



# Collect the first_name of the user.
# If first_name is blank, print "You must enter a first name"


# first_name = input("Enter your first name:").strip()

# if not first_name:
#     print("you must enter a first name")


# Guido Van Rossum

# is_young = False
# print("You are young" if is_young else "You are old")
# print("You are young") if is_young else print("You are old")


# is_male = False
# pronoun = "He" if is_male else "She"
# print(f"Pronoun is {pronoun}")


# age = 19
# is_male = True

# if is_male:
#     if age >= 18:
#         print("You are male and you can vote")
#     else:
#         print("You are male but you are not of age to vote")
# else:
#     print("Women cannot vote")


# is_male = True
# if is_male:
#     # to do: add code here
#     pass
# print("Some other code")

# Exercise 1
# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manu


# Exercise 2
# Ask the user to enter their age, and if they are 18 or above, print "you are of voting age"
# otherwise, print "you cannot vote yet"


# Exercise 3
# Ask the user to enter a number, and print True if the number is divisible by 5 exactly.
# Otherwise, print False.


# Exercise 4
# Ask the user to enter the temperature in Celsius.
# If the temp is 30 or more then print "It's hot! Wear light clothes"
# If the temp is between 20 and 29, print "It's warm. A t-shirt should be fine"
# If the temp is between 10 and 19, print "It's a bit chilly. Wear a jacket"
# If the temp is below 10, print "It's cold! Wear a coat and stay warm."


# ----------------------------------ASSIGNMENT CORRECTION---------------------------------------------
# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
# # elif a or (b > 0):  # wrong
#     print("Only one is positive")
# else:
#     print("Neither is positive")


# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x, y, z = input("Enter three numbers separated by commas: ").split(",")
# x, y, z = int(x), int(y), int(z)
# if x > y > z:
#     print("Decreasing order")
# elif x < y < z:
#     print("Increasing order")
# else:
#     print('Neither')

# 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# palindrome = input("Enter some text: ").strip().lower().replace(" ", "")
# if palindrome == palindrome[::-1]:
#     print("Is a palindrome")
# else:
#     print("not a palindrome")

# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.

# x = input("Enter the value of x: ").strip()
# y = input("Enter the value of y: ").strip()
# z = input("Enter the value of z: ").strip()

# if x == y == z:
#     print("All same")
# elif x != y and y != z and x != z:
#     print("All different")
# else:
#     print("Two are equal")



# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = float(input('Enter the value of the first angle: '))
# angle2 = float(input('Enter the value of the second angle: '))
# angle3 = float(input('Enter the value of the third angle: '))

# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 == 180):
#     print("Valid triangle")
# else:
#     print("Invalid triangle")


# 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.

# ch = input("Enter a single character: ").strip().lower()

# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# import string

# alphabets = string.ascii_lowercase

# ch = input("Enter a single character: ").strip().lower()


# if len(ch) > 1:
#     print("You must enter a single character alphabet")
# elif ch not in alphabets:
#     print("Not an alphabet")
# elif ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".

# color1, color2, color3 = input("Enter three colors separated by commas: ").split(",")
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()

# primary_colors = ("red", "blue", "yellow")

# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# Without repeating any color version
# colors = input("Enter three colors separated by commas: ").split(",")
# if len(colors) != 3:
#     print("Enter three colors")
# else:
#     color1, color2, color3 = colors
#     color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()

#     primary_colors = {"red", "blue", "yellow"}
#     colors = {color1, color2, color3}


#     if colors.issubset(primary_colors):
#         if len(colors) != 3:
#             print("All colors must be unique")
#         else:
#             print("All primary colors, no repitition")
#     else:
#         print("Not all primary colors")

# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".


# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# message = input('Enter a message: ').strip().upper()

# if "URGENT" in message or "IMPORTANT" in message or "IMMEDIATE" in message:
#     print("High priority message")
# else:
#     print("Normal message")



# 10. You have two variables, status1 and status2, provided through user input, each of 
# which can be "active", “inactive", or "pending". Write an if statement to print 
# "Both active" if both statuses are "active", "One active" if exactly one is "active",
# and "None active" if neither is "active".

# status1 = input("Enter the value of status 1 (either active, inactive or pending): ").strip().lower()
# status2 = input("Enter the value of status 2 (either active, inactive or pending): ").strip().lower()

# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print("One active")
# else:
#     print("None active")


# 11. Given a string `filename` supplied by the user, write an if statement to check if the
# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# print "Not an image file".

# filename = input("Enter the file name: ").strip().lower()
# if filename.endswith((".jpg", ".png", ".gif")):
# # if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
#     print('Image file')
# else:
#     print("Not an image file")


# 12. You have a variable `access_level` provided through user input which can be "admin",
# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# "admin", "Limited access" if it is "user", and "No access" if it is "guest".

# 13. Given a string `email` collected from the user, write an if statement to check if the
# email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# print "Invalid email".

# email = input("Enter email address: ").strip()

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# 14. You have a variable `day` provided by user input which can be any day of the week 
# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# day = input("Enter any day of the week: ").strip().capitalize()

# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# weekend = ["Saturday", "Sunday"]

# if day in weekdays:
#     print("Weekday")
# elif day in weekend: 
#     print("Weekend")
# else:
#     print("Not a day of the week")


# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# input from the user and prints the greatest number. Use conditional statements
# to determine which number is the greatest. Bonus point if you can do it without `else` 
# statements.

# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = int(num1), int(num2), int(num3)

# if num1 >= num2 and num1 >= num3:
#     print("num1 is the greatest")
# elif num2 >= num1 and num2 >= num3:
#     print("num2 is the greatest")
# else:
#     print("num3 is the greatest")

# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = int(num1), int(num2), int(num3)

# greatest = num1

# if num2 > greatest:
#     greatest = num2

# if num3 > greatest:
#     greatest = num3

# print(f"{greatest} is the greatest")

# ----------------------------------ASSIGNMENT CORRECTION---------------------------------------------


# ----------------------------------MORE EXERCISES---------------------------------------------
# Exercise 1: Login Verification
# Ask the user to enter a username and password.
# If both match the expected values, print "Login successful".
# Otherwise, print "Invalid credentials".
# Sample input: user123 pass123
# Sample output: "Login successful"
# Sample input: user123 wrongpass
# Sample output: "Invalid credentials"


# Exercise 2: ATM Withdrawal Conditions
# Ask the user how much they want to withdraw.
# - If amount is more than 100000, print "Limit exceeded"
# - If amount is not a multiple of 100, print "Amount must be multiple of 100"
# - If amount is valid, print "Processing withdrawal of [amount]"
# Sample input: 250
# Sample output: "Processing withdrawal of 250"


# Exercise 3: Check Two strings Have the Same Last character
# Write a program that takes two strings and checks if they end in the same character.
# Sample input: Fine wine
# Sample output: "Same last character"
# Sample input: Hello Nina
# Sample output: "Different last characters"
# ----------------------------------MORE EXERCISES---------------------------------------------

