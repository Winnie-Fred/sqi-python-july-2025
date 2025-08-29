#                        List           Tuple                   Dictionaries

# Mutable?               Yes            No                          Yes
# Ordered?               Yes            Yes                         Yes (in recent versions of Python)
# Indexed?               Yes            Yes                         Yes (but with their keys)
# Allow duplicates?      Yes            Yes                         Allows duplicate values, but not duplicate keys



phone_book = {"Olaitan": "07052497358", "Mr. Dan": "08132932399", 0: "zero"}
# print(phone_book["Mr. Dan"])
# print(phone_book[0])

phone_book["Mr. Dan"] = "08176845609"
# print(phone_book)


phone_book["Winnie"] = "09030556547"
# print(phone_book)

del phone_book["Olaitan"]
# print(phone_book)


# print("Winnie" in phone_book)
# print("Winnie" in phone_book.keys())
# print("09030556547" in phone_book.values())
# print("Olaitan" in phone_book)
# print("Olaitan" in phone_book.keys())
# print("08132932399" in phone_book.values())


# print(phone_book.keys())  # dict_keys 
# print(type(phone_book.keys()))  # dict_keys 
# print(phone_book.values())  # dict_values
# print(type(phone_book.values()))  # dict_values
# keys = list(phone_book.keys())
# print(keys)
# values = list(phone_book.values())
# print(values)

# items = list(phone_book.items())  # dict_items
# print(items)
# print(type(items))
# print(list(items))

# (mr_dan, mr_dan_no), *_ = items
# print(mr_dan)
# print(mr_dan_no)




# phone_book = {"Olaitan": "07052497358", "Mr. Dan": "08132932399", 0: "zero", "olaitan": "07052497300"}
# phone_book = {"Olaitan": "07052497358", "Mr. Dan": "07052497358", 0: "zero", "olaitan": "07052497300"}
# print(phone_book)



# phone_book = {("one", "two", "three"): [1, 2, 3], ("four", "five", "six"): [4, 5, 6]}

# phone_book = {"Olaitan": ["07052497358", "08067654522"], "Mr. Dan": ["08132932399", "09076590532"]}



# english_dictionary = {
#     "set": [
#             # As a verb
#             "to put (something) in a particular place or position",
#             "to cause to be in a specified condition",
#             "to arrange or fix definitely",
#             "to adjust or fix (a device, alarm, etc.) to operate",
#             "to establish (rules, standards, records, etc.)",
#             "to prepare (something) to be used or activated",
#             "to cause (a gel, concrete, etc.) to harden or solidify",
#             "to place (a broken bone) so it can heal",
#             "to assign or decide on (a task, price, date, etc.)",
#             "to direct (someone) to begin doing something",
#             "to start (a machine or device)",
#             "to arrange hair into a desired style using rollers or gel",
#             "to present a scene in a play, movie, or story",
            
#             # As a noun
#             "a group or collection of things that belong together",
#             "a group of people with shared interests or social class",
#             "a device or piece of equipment (e.g., television set)",
#             "the arrangement of scenery and props on a stage or film",
#             "a fixed or established way of doing something",
#             "a number of repetitions in weight training or exercise",
#             "a mathematical collection of distinct elements",
#             "a group of similar items sold as a unit (e.g., a set of dishes)",
#             "the way in which a play is staged or directed",
#             "a session or group of songs performed (e.g., in music)",
#             "a part of a match in sports (e.g., tennis, volleyball)",
#             "the act of setting something in place or condition",
#             "the posture or carriage of a person or thing",
            
#             # As an adjective
#             "fixed or arranged in advance",
#             "ready or prepared to begin",
#             "intent or determined",
#             "having a fixed expression or look",
#             "firmly placed or mounted",
#             "customary or standard",
            
#             # Idioms / figurative meanings
#             "set in stone – fixed or unchangeable",
#             "set the stage – create the conditions for something",
#             "set one's sights on – to aim for or desire something",
#             "set apart – to distinguish or separate",
#             "set off – to cause to start (e.g., an alarm or event)",
#             "set up – to establish, arrange, or trick someone",
#             "set down – to write or record",
#             "set out – to begin a journey or attempt"
#     ],
#     "boy": [
#                 # Literal meanings
#                 "a male child",
#                 "a young male person, typically under the age of 18",
#                 "a son",
#                 "a male servant or employee (dated or offensive in some contexts)",
#                 "a young male worker, especially in informal or historical usage (e.g., office boy)",
                
#                 # Colloquial and figurative uses
#                 "a man, especially when referred to informally or affectionately (e.g., 'he's a good boy')",
#                 "used to refer to a male romantic partner affectionately (e.g., 'my boy')",
#                 "a member of a male group or team (e.g., 'the boys in blue' for police)",
#                 "used to express excitement or emphasis (e.g., 'Oh boy!')",
#                 "a nickname or identifier among close friends (e.g., 'he’s one of the boys')",
                
#                 # Cultural and historical usage
#                 "used in some cultures or colonial contexts to refer to a male servant or subordinate (now considered offensive)",
#                 "in racial contexts, especially in American history, used derogatorily to demean adult Black men (offensive)",
                
#                 # Idioms and expressions
#                 "golden boy – a favored or successful young man",
#                 "mama's boy – a man excessively attached to his mother",
#                 "boys will be boys – used to excuse or explain immature or rowdy male behavior",
#                 "old boy – a male former student of a school, especially a private one in Britain",
#                 "boy wonder – a very young person who is unusually successful or talented",
#                 "bad boy – a rebellious or nonconforming man",
                
#                 # Pop culture references (non-exhaustive, just common ones)
#                 "used in branding or entertainment (e.g., 'The Boy' as a movie title)",
#                 "in K-pop or other fandoms, 'boy' refers to male idols or boy groups"
#     ]

# }


# print(english_dictionary)
# print(english_dictionary["set"])
# print(english_dictionary["set"][0])

# my_dict = {}
# print(type(my_dict))

# my_set = set()
# my_set = {1, 8, 79, 2, 9}

# bank_record = {
#     "Winnie": {
#         "balance": 1000,
#         "account_number": "0811020150",
#         "bank": "Access Bank",
#         "is_savings_account": True
#     },
#     "Olaitan": {
#         "balance": 4000,
#         "account_number": "1018302637",
#         "bank": "FCMB",
#         "is_savings_account": False
#     },

# }

# Create a bank_record system using a dictionary where the account owner is the 
# key and the account details are another dictionary. The account details dictionary
# has the following keys: balance, account number, bank, is_savings_account



# 1. Ask the user to enter whose details they want to view. 
# 2. Ask the user to enter either balance, account_number, bank or is_savings_account
# 3. Example: User chose "Winnie" as user whose details to view, and "balance"
# bank_record["Winnie"]["balance"]


# bank_record = {
#     "Winnie": {
#         "balance": 1000,
#         "account_number": "0811020150",
#         "bank": "Access Bank",
#         "is_savings_account": True
#     },
#     "Olaitan": {
#         "balance": 4000,
#         "account_number": "1018302637",
#         "bank": "FCMB",
#         "is_savings_account": False
#     },
# }

# account_owner = input("Enter the name of the accoutn owner: ").strip()
# key = input("Choose between balnce, account_number, bank and is_savings_account: ").strip()

# print(bank_record[account_owner][key])



# account_owner = input("Enter the new account owner: ").strip()
# balance = int(input(f"Enter the balance of {account_owner}: "))
# bank = input(f"Enter the bank of {account_owner}: ")
# account_number = input(f"Enter the account number of {account_owner}: ")
# is_savings_account = bool(int(input("Enter 0 for False or 1 for True if account is a savings account: ")))

# bank_record[account_owner] = {
#     "balance": balance,
#     "account_number": account_number,
#     "bank": bank,
#     "is_savings_account": is_savings_account
# }

# print(bank_record)


# Ask the user for the account owner whose details they want to update.
# Ask them for the field they want to update i.e. account_number or bank.
# Update the record.
# Print the bank_revord variable. 

# bank_record = {
#     "Winnie": {
#         "balance": 1000,
#         "account_number": "0811020150",
#         "bank": "Access Bank",
#         "is_savings_account": True
#     },
#     "Olaitan": {
#         "balance": 4000,
#         "account_number": "1018302637",
#         "bank": "FCMB",
#         "is_savings_account": False
#     },
# }

# account_owner = input("Enter the account owner whose details you wish to update: ").strip()  # Winnie
# key = input("Choose between account_number and bank: ").strip()  # account_number
# new_value = input("Enter the new value: ")  # 9030556547

# bank_record[account_owner][key] = new_value

# print(bank_record)



# Create a dictionary called my_dream_car containing the keys brand, manufacture_year, is_electric
# and whatever values you want for your dream car
# Add a new key "color" and set it to the color of your dream car
# Change the value of is_electric key to the opposite of whatever was there before
# Also change the car's manufacture year to 1987
# Get rid of the color key.




# grades = [90, 34, 78, 13, 89]
# average_grade = sum(grades) / len(grades)
# max_grade = max(grades)
# min_grade = min(grades)

# print(f"The average grade in the class is: {average_grade}")
# print(f"The maximum grade in the class is: {max_grade}")
# print(f"The minimum grade in the class is: {min_grade}")


# student_grades = {"James": 90, "Lola": 34, "Seun": 78, "Olaitan": 13, "David": 89}
# student_with_max_grade = max(student_grades, key=student_grades.get)
# print(f"The student with the maximum grade in the class is: {student_with_max_grade}")


# ----------------------------------.get()---------------------------------------------

# my_dream_house = {
#     'type': 'mansion',
#     'no_of_rooms': 8,
#     'has_pool': True,
#     'has_garage': True,
#     'location': 'Lekki'
# }

# print(my_dream_house["no_of_rooms"])
# print(my_dream_house["no of rooms"])
# print('no_of_garages' in my_dream_house)
# if 'no_of_garages' in my_dream_house:
#     print(my_dream_house['no_of_garages'])

# print(my_dream_house.get('no_of_garages', 0))
# print(my_dream_house.get('location', 'No location yet'))

# has_pool = my_dream_house.get('has_pool')
# print(has_pool)

# has_roof = my_dream_house.get('has_roof', 'Building not complete')
# print(has_roof)

# ----------------------------------.get()---------------------------------------------



# ----------------------------------.setdefault()---------------------------------------------
# my_dream_house = {
#     'type': 'mansion',
#     'no_of_rooms': 8,
#     'has_pool': True,
#     'has_garage': True,
#     'location': 'Lekki'
# }


# print(my_dream_house.setdefault('type'))
# print(my_dream_house.setdefault('has_roof', False))
# print(my_dream_house.setdefault('has_roof'))
# print(my_dream_house)

# ----------------------------------.setdefault()---------------------------------------------


# ----------------------------------updating a dict---------------------------------------------


# # Method 1 - square bracket notation
# sqi_dugbe = {
#     "no_of_instructors": 15,
#     "no_of_students": 70,
#     "no_of_depts": 10,
#     "location": "Heritage Mall, Dugbe"
# }


# sqi_dugbe["no_of_depts"] = 20
# print(sqi_dugbe)


# Method 2 - .update with kwargs
# kwargs - keyword arguments

# sqi_dugbe = {
#     "no of instructors": 15,
#     "no_of_students": 70,
#     "no_of_depts": 10,
#     "location": "Heritage Mall, Dugbe"
# }
# sqi_dugbe.update(no_of_depts=20)
# print(sqi_dugbe)
# sqi_dugbe.update(has_staff_wifi=True, no_of_instructors=78)
# print(sqi_dugbe)


# Method 3 - .update with dict
# sqi_dugbe = {
#     "no of instructors": 15,
#     "no_of_students": 70,
#     "no_of_depts": 10,
#     "location": "Heritage Mall, Dugbe"
# }
# sqi_dugbe.update({'no_of_depts':20})
# sqi_dugbe.update({'no of instructors': 120})
# sqi_dugbe.update({'is_open': True})
# print(sqi_dugbe)

# ----------------------------------updating a dict---------------------------------------------


# ----------------------------------removing from a dict---------------------------------------------


# Method 1 - using the del keyword
# lion = {
#     'is_wild': True,
#     'no_of_legs': 4,
#     'is_friendly': False,
#     'is_predator': True,
# }
# del lion['is_friendly']
# print(lion)

# del lion
# print(lion)

# Method 2 - using the .pop() method
# lion = {
#     'is_wild': True,
#     'no_of_legs': 4,
#     'is_friendly': False,
#     'is_predator': True,
# }

# result = lion.pop('is_predator')
# print(result)
# print(lion)


# Method 3 - using the .popitem() method
# lion = {
#     'is_wild': True,
#     'no_of_legs': 4,
#     'is_friendly': False,
#     'is_predator': True,
# }
# result = lion.popitem()
# print(result)
# print(lion)
# result = lion.popitem()
# print(result)
# print(lion)
# ----------------------------------removing from a dict---------------------------------------------



# ----------------------------------miscellaneous---------------------------------------------
# lion = {
#     'is_wild': True,
#     'no_of_legs': 4,
#     'is_friendly': False,
#     'is_predator': True,
# }
# print(len(lion))
# print(type(lion))


# names = ["James", "John", "Daniel", "Taylor"]
# names = [("James", 34), ("John", 78), ("Daniel", 65), ("Taylor", 24)]
# names = (("James", 34), ("John", 78), ("Daniel", 65), ("Taylor", 24))
# names = {("James", 34), ("John", 78), ("Daniel", 65), ("Taylor", 24)}
# print(dict(names))

# names = dict(james=34, john=78, daniel=65, taylor=24)
# print(names)

# ----------------------------------miscellaneous---------------------------------------------

# ----------------------------------clear a dict---------------------------------------------

# Method 1 - .clear()
# people_ages = {'james': 34, 'john': 78, 'daniel': 65, 'taylor': 24}
# print(people_ages)
# people_ages.clear()
# print(people_ages)


# Method 2 - override with an empty list
# people_ages = {'james': 34, 'john': 78, 'daniel': 65, 'taylor': 24}
# print(people_ages)
# people_ages = {}
# print(people_ages)
# ----------------------------------clear a dict---------------------------------------------


# ----------------------------------copy a dict---------------------------------------------
# people_ages = {'james': 34, 'john': 78, 'daniel': 65, 'taylor': 24}
# people_ages_duplicate = people_ages  # reference, not true copy
# print(people_ages is people_ages_duplicate)



# people_ages = {'james': 34, 'john': 78, 'daniel': 65, 'taylor': 24}
# people_ages_duplicate = people_ages.copy()  # true copy
# print(people_ages is people_ages_duplicate)

# import copy

# people_ages = {'james': 34, 'john': 78, 'daniel': 65, 'taylor': 24}
# people_ages_duplicate = copy.deepcopy(people_ages)  # true copy
# print(people_ages is people_ages_duplicate)

# ----------------------------------copy a dict---------------------------------------------



# ----------------------------------nested dicts quiz correction---------------------------------------------

# 1. Access and print the name of the teacher of "class2".
# school = {
#     "class1": {
#         "students": ["Alice", "Bob"],
#         "teacher": "Mr. Smith"
#     },
#     "class2": {
#         "students": ["Charlie", "David"],
#         "teacher": "Ms. Johnson"
#     }
# }


# # 2. Access and print the second employee in the "Engineering" department.
# company = {
#     "HR": ["Alice", "Bob"],
#     "Engineering": ["Charlie", "David"]
# }


# # 3. Access and print the name of the second assistant.
# university = {
#     "faculty": {
#         "professors": ["Dr. Smith", "Dr. Brown"],
#         "assistants": ["Ms. Green", "Mr. White"]
#     },
#     "students": ["John", "Jane", "Alice", "Bob"]
# }


# # 4. Access and print the price of the third fruit.
# store = {
#     "fruits": [
#         {"name": "apple", "price": 0.5},
#         {"name": "banana", "price": 0.2},
#         {"name": "cherry", "price": 1.5}
#     ],
#     "vegetables": [
#         {"name": "carrot", "price": 0.3},
#         {"name": "lettuce", "price": 1.0},
#         {"name": "onion", "price": 0.4}
#     ]
# }


# # 5. Access and print the second non-fiction book.
# library = {
#     "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
#     "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
# }


# # 6. Access and print the age of the first child.
# family = {
#     "parents": ["John", "Jane"],
#     "children": [
#         {"name": "Tom", "age": 5},
#         {"name": "Lucy", "age": 8}
#     ]
# }


# # 7. Access and print the name of the second main course.
# restaurant = {
#     "menu": {
#         "appetizers": ["soup", "salad"],
#         "main_courses": ["steak", "pasta"],
#         "desserts": ["cake", "ice cream"]
#     },
#     "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
# }


# # 8. Access and print the department of the user of the first desk.
# workspace = {
#     "desks": [
#         {"user": "Alice", "department": "HR"},
#         {"user": "Bob", "department": "Engineering"}
#     ],
#     "equipment": {"computers": 20, "printers": 10}
# }


# # 9. Access and print the name of the second designer.
# team = {
#     "developers": ["Dev A", "Dev B"],
#     "designers": ["Designer X", "Designer Y"],
#     "projects": ["Project 1", "Project 2"]
# }


# # 10. Access and print the second international destination.
# travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
# {"flights": 1500, "hotels": 2000}}

# ----------------------------------nested dicts quiz correction---------------------------------------------



# ----------------------------------exercise---------------------------------------------

movies = []

# Ask 3 friends to provide the following details:
# "title" (string)
# "duration" (float, in hours)
# "genre" (string)


# Add this as a dictionary into the movie list
# Do for all 3 friends 

# movies = [
#     {"title": "Avengers", "duration": 2.00, "genre": "action"},
#     {"title": "Get Out", "duration": 2.00, "genre": "horror"},
#     {"title": "Koto aye", "duration": 3.40, "genre": "horror"},
# ]

# 1st friend

# title = input("Enter the movie title: ").strip()
# duration = float(input("Enter the duration of the movie: "))
# genre = input("Enter the movie genre: ").strip()

# movies.append({"title": title, "duration": duration, "genre": genre})

# # 2nd friend
# title = input("Enter the movie title: ").strip()
# duration = float(input("Enter the duration of the movie: "))
# genre = input("Enter the movie genre: ").strip()

# movies.append({"title": title, "duration": duration, "genre": genre})
# # 3rd friend
# movies.append({"title": title, "duration": duration, "genre": genre})
# title = input("Enter the movie title: ").strip()
# duration = float(input("Enter the duration of the movie: "))
# genre = input("Enter the movie genre: ").strip()

# movies.append({"title": title, "duration": duration, "genre": genre})

# print(movies)
# ----------------------------------exercise---------------------------------------------

# ----------------------------------ASSIGNMENT CORRECTION---------------------------------------------
# 1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".

# student = {
#     "name": "John",
#     "age": 20,
#     "grade": "A"
# }
# print(student.get("name"))
# print(student["name"])
# print(student.setdefault("name"))


# 2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# product = {"name": "Laptop", "price": 999.99, "stock": 50}
# product["price"] = 899.99


# 3. Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee = {"name": "Alice", "position": "Manager"}
# employee.update({'salary': 50000})
# employee.update(salary=50000)
# employee.setdefault("salary", 50000)
# employee["salary"] = 50000
# print(employee)

# 4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10, "banana": 5, "orange": 8}
# del inventory["banana"]
# result = inventory.pop("banana")
# print(result)
# print(inventory)

# 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.

# person = {'name': 'Bob', "age": 25, "city": "New York"}
# person_copy = person.copy()

# 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".

# family = {
#     "child1": {
#         "name": "Winifred",
#         "age": 23
#     },
#     "child2": {
#         "name": "Justin",
#         "age": 22
#     },
#     "child3": {
#         "name": "Augusta",
#         "age": 20
#     }
# }
# print(family["child2"]["age"])


# 7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".

# car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
# print(car["model"])

# 8. Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# 9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# 10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# 12. Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
# 13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.

# grades = {"math": "A", "science": "B", "history": "C"}
# # print(list(grades.keys()))
# print(grades.keys())


# 14. Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
# 15. Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.

# ----------------------------------ASSIGNMENT CORRECTION---------------------------------------------