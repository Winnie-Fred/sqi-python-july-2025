# with open("random_users.csv") as csc_data:
# with open("random_users.csv", "r") as f:
#     # data = f.read()
#     data = f.readlines()

# print(data)




# with open("my_story.txt", "w") as f:
#     f.write("My name is Winnie\nI am teaching Python at SQI.\nToday is Monday")

# f = open("my_story.txt", "r")

# contents = f.read()
# print(contents)

# f.close()


# with - context manager

# Read from any existing Python file
# And print the contents to the terminal

# Write "My name is {name}" to a new file called "intro.docx"
# Append to the same file "I am learning Python"


# try:
#     with open("eycnkmx.txt", "r") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError as e:
#     print(f"File does not exist: {e}")


# f = None

# try:
#     f = open("y3bfncmk.txt", "r")
# except FileNotFoundError as e:
#     print(f"File does not exist: {e}")
# else:
#     data = f.read()
#     print(data)
# finally:
#     if f is not None:
#         f.close()        

# a = None
# b = None
# # print(b is not None)
# print(not b)

# from datetime import datetime, timedelta

# # from helpers import _format_date, _pretty_print_row

# import helpers as utils

# now = datetime.now()

# helpers = ""

# with open("random_users.csv", "r") as f:
#     lines = f.readlines()

# lines = lines[1:]
# longest_time_spent = timedelta(0)
# longest_served_customer = ""
# for row in lines:
#     row = row.strip()
#     user_id, name, email, age, country, signup_date = row.split(",")
#     signup_date = utils._format_date(signup_date)
#     time_spent = now - signup_date
#     if time_spent > longest_time_spent:
#         longest_time_spent = time_spent
#         longest_served_customer = name
#     print(utils._pretty_print_row(name, time_spent))

# print(f"The longest served customer is {longest_served_customer}")



# import os

# from pathlib import Path

# print(os.mkdir("new_folder"))

# os.rmdir()


# from pathlib import Path

# path = Path("C:/Users/dell/Documents/SQI/SQI_PYTHON_MAY_2025/data_analyst/extracter.py")
# with open(path, "r") as f:
#     print(f.read())



# import datetime

# yesterday = datetime.date(2025, 8, 25)

# print(yesterday)
# print(type(yesterday))

# import datetime


# birth_date = input("Enter the date in this format DD-MM: ").strip()
# birth_date = birth_date + f"-{datetime.datetime.now().year}"
# birth_date = datetime.datetime.strptime(birth_date, "%d-%m-%Y").date()
# # print(birth_date)


# today = datetime.datetime.now().date()

# if birth_date < today:
#     print("Your birthday has passed this year")
# elif birth_date == today:
#     print("happy birthday to you")
# else:
#     print("Your birthday is not here yet")

# import datetime

# two_weeks_ago = datetime.datetime.now() - datetime.timedelta(14)

# # formatted_time = two_weeks_ago.strftime("%Y/%f/%d")
# # formatted_time = two_weeks_ago.strftime("%d/%m/%Y")
# formatted_time = two_weeks_ago.strftime("%d/%m/%Y  %H:%M:%S")

# print(formatted_time)


# name = "Winnie"
# age = 25

# print("My name is %s and I am %d years old." % (name, age))




# import math

# print(math.sqrt(16))
# print(math.sqrt(25))
# print(math.sqrt(36))
# print(math.sqrt(17))

# print(math.radians(180))

# print(math.log(12))
# print(math.log10(100))

# print(math.pi)
# print(math.e)


# PSL - python standard library

# import json



# users = [
#     {
#         "id": 1,
#         "name": "Alice Johnson",
#         "age": 28,
#         "gender": "Female",
#         "email": "alice.johnson@example.com",
#         "hobbies": ["reading", "hiking", "painting"]
#     },
#     {
#         "id": 2,
#         "name": "Brian Smith",
#         "age": 34,
#         "gender": "Male",
#         "email": "brian.smith@example.com",
#         "hobbies": ["gaming", "cycling", "cooking"]
#     },
#     {
#         "id": 3,
#         "name": "Cynthia Lee",
#         "age": 22,
#         "gender": "Non-binary",
#         "email": "cynthia.lee@example.com",
#         "hobbies": ["photography", "traveling"]
#     },
#     {
#         "id": 4,
#         "name": "David Brown",
#         "age": 41,
#         "gender": "Male",
#         "email": "david.brown@example.com",
#         "hobbies": ["chess", "running", "gardening"]
#     },
#     {
#         "id": 5,
#         "name": "Ella Martinez",
#         "age": 29,
#         'gender': "Female",
#         "email": "ella.martinez@example.com",
#         "hobbies": ["yoga", "music", "swimming"]
#     }
# ]
# print(type(users))

# with open("random_users.csv", "r") as f:
#     contents = f.read()

# with open("dump.json", "w") as f:
#     f.write(json.dumps(contents, indent=6))


# ----------------------------------------HOW TO TURN CSV TO JSON----------------------------------------

# import json
# with open("random_users.csv", "r") as f:
#     lines = f.readlines()


# data = []

# headers = lines[0]
# lines = lines[1:]
# for row in lines:
#     row = row.strip()
#     user_id, name, email, age, country, signup_date = row.split(",")
#     data.append({"id": int(user_id), "name": name, "email": email, "age": int(age), "country": country, "signup_date": signup_date})


# with open("random_users.json", "w") as f:
#     f.write(json.dumps(data, indent=4))


# ----------------------------------------HOW TO TURN CSV TO JSON----------------------------------------


# pip - pip installs python

# import sys


# for path in sys.path:
#     print(path)




