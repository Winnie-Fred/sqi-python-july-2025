# Lists

# Mutable? - Yes
# Ordered? - Yes
# Indexed? - Yes
# Allow duplicates? - Yes


# Tuples
# Mutable? - No
# Ordered? - Yes
# Indexed? - Yes
# Allow Duplicates? - Yes

# colors = ("red", "green", "blue", "violet")
# colors = "red", "green", "blue", "violet"
# colors = "red",
# print(type(colors))


# colors = ("red", "green", "red", "blue", "violet")
# print(colors)
# print(colors[-2])
# colors[-2] = "purple"
# color = "purple"
# color[2] = "u"


# colors = ("red", "green", "red", "blue", "violet")
# print(len(colors))


# colors = ("red", True, "green", "red", "blue", 65,9, "violet")

# colors = ["red", "green", "red", "blue", "violet"]
# print(type(colors))
# colors = tuple(colors)
# print(type(colors))

# colors = ("red", "green", "red", "blue", "violet")

# colors = list(colors)
# colors.append("silver")
# colors = tuple(colors)
# print(colors)


# football_clubs = ("Real Madrid", "Barca", "Athletico Madrid")
# others = ("Chelsea", "Arsenal", "Manchester United")

# all_clubs = football_clubs + others
# print(all_clubs)

# football_clubs = ("Real Madrid", "Barca", "Athletico Madrid") * 6
# football_clubs = ["Real Madrid", "Barca", "Athletico Madrid"] * 6
# print(football_clubs)

# football_clubs = ("Real Madrid", "Barca", "Athletico Madrid") ** 2  # doesn't work
# print(football_clubs)

# letters = "abcde"
# print(letters * 5)

# ==================================UNPACKING A TUPLE=============================================================
# musicians = ("Davido", "Wizkid", "Burna boy", "Olamide", "Rema")
# obo = musicians[0]
# wizzy = musicians[1]
# burna = musicians[2]
# baddo = musicians[3]
# rema = musicians[4]

# print("obo: ", obo)
# print("wizzy: ", wizzy)
# print("burna: ", burna)
# print("baddo: ", baddo)
# print("rema: ", rema)


# musicians = ("Davido", "Wizkid", "Burna boy", "Olamide", "Rema")
# obo, wizzy, burna, baddo, rema = ("Davido", "Wizkid", "Burna boy", "Olamide", "Rema")

# print("obo: ", obo)
# print("wizzy: ", wizzy)
# print("burna: ", burna)
# print("baddo: ", baddo)
# print("rema: ", rema)


# obo, wizzy, burna, baddo, rema, ruger = ("Davido", "Wizkid", "Burna boy", "Olamide", "Rema", "Ruger")


# print("obo: ", obo)
# print("wizzy: ", wizzy)
# print("burna: ", burna)
# print("baddo: ", baddo)
# print("rema: ", rema)
# print("ruger: ", ruger)


# Create a tuple called 'appliances' containing "pressing iron", "electric kettle", "pressure cooker", "oven" in this order

# Unpack the tuple into variables iron, kettle, cooker and oven respectively.
# Print the values of all the variables.

# appliances = ("pressing iron", "electric kettle", "pressure cooker", "oven")
# iron, kettle, cooker, oven = appliances
# print("iron:", iron)
# print("kettle:", kettle)
# print("cooker:", cooker)
# print("oven:", oven)


# appliances = ("pressing iron", "electric kettle", "pressure cooker", "oven")
# iron, kettle, _, oven = appliances
# print("iron:", iron)
# print("kettle:", kettle)
# print("cooker:", _)
# print("oven:", oven)


# appliances = ("pressing iron", "electric kettle", "pressure cooker", "oven")
# appliances = ["pressing iron", "electric kettle", "pressure cooker", "oven"]
# # iron, *_, oven = appliances
# iron, _, cooker, _ = appliances
# print("iron:", iron)
# print("_:", _)
# print("cooker:", cooker)


# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])

# name, age_position, depts = record

# age, position = age_position
# first_dept, second_dept = depts

# print(age)
# print(first_dept)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])

# # name, (age, position), (first_dept, second_dept) = record
# _, (age, _), (first_dept, _) = record

# print(age)
# print(first_dept)


# 8. Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.


info = ("product123", ("Electronics", 299.99), (20, 5, 2022))



# ==================================UNPACKING A TUPLE=============================================================
# appliances = ("pressing iron", "electric kettle", "pressure cooker", "oven")
# # iron, _, _, oven = appliances
# # iron, *_, oven = appliances
# iron, *others, oven = appliances
# print(iron)
# print(others)
# print(oven)

# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, age_position, depts = record
# age = age_position[0]
# hr = depts[0]
# print(age)
# print(hr)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, age_position, depts = record
# age, position = age_position
# dept1, dept2 = depts
# print(age)
# print(dept1)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (dept1, dept2) = record
# print(age)
# print(dept1)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# _, (age, _), (dept1, _) = record
# print(age)
# print(dept1)
# ==================================UNPACKING A TUPLE=============================================================




# ==================================ASSIGNMENT CORRECTION=============================================================
# 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
# dimensions = 10, 20, 30
# length, width, height = dimensions
# print(length)
# print(width)
# print(height)


# 2. Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.

# coordinates = (1.5, 2.5, 3.5)
# x, y, z = coordinates
# print(y)


# 3. Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# person = ("John", 25, "Engineer")
# name, age, profession = person
# print(profession)


# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.

# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# (student1, student2), _, _ = data 
# print(student2)

# 5. Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")

# color1, color2, *_ = colors
# print(color1)
# print(color2)
# print(_)


# 6. Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])

# _, (age, _), (dept1, _) = record
# print(age)
# print(dept1)


# 7. Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.

# triplet = ("one", "two", "three")
# _, second, _ = triplet
# print(second)

# 8. Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# _, (category, _), (*_, year) = info
# print(category)
# print(year)


# 9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# *_, (_, last) = nested_tuple
# print(last)



# 10. Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# _, (_, qty_bananas), _ = inventory
# print(qty_bananas)

# ==================================ASSIGNMENT CORRECTION=============================================================




# my_tuple = (["one", "two"], ["three"], ["four", "five"])
# # my_tuple[0] = ["seven", "eight"]
# my_tuple[0][0] = "seven"
# print(my_tuple)