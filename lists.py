# ==================================INTRO=============================================================
# my_list = list("dance")
# print(my_list)



# Shopping List
# 
# shopping_list = ["rice", "tomato", "pepper", "onions", "garlic", "maggi", "butter", "onions", "vegetables"]
# print(shopping_list[4])
# print(shopping_list[4][2])
# print(shopping_list[-1])
# print(shopping_list[-1][4])

# print("before: ", shopping_list)
# shopping_list[-2] = "groundnut oil"
# shopping_list.append("curry")
# shopping_list.insert(3, "curry")
# shopping_list.insert(0, "curry")
# shopping_list.remove("onions")
# shopping_list.remove("garlic")
# print("garlic" in shopping_list)
# print("egfvbyenjd" in shopping_list)
# print("after:  ", shopping_list)
# is_happy = False
# print("Yes" if is_happy else "No")

# Create a list called means_of_transport containing "plane", "ship", "car", "train"
# in this exact order.
# Print the list after every step below:
# means_of_transport = ["plane", "ship", "car", "train"]
# 1. Add a new means of transport "camel" to the end of the list
# means_of_transport.append("camel")
# print(means_of_transport)

# # 2. Remove "car" from the list
# means_of_transport.remove("car")
# print(means_of_transport)


# # 3. Add "lorry" in between "plane" and "ship"
# means_of_transport.insert(1, "lorry")
# print(means_of_transport)

# # 4. Check if "helicopter" is in the list
# print("helicopter" in means_of_transport)

# # 5. Change "plane" to "aeroplane"
# means_of_transport[0] = "aeroplane"
# print(means_of_transport)

# # 6. Print a list of the first 3 means of transport in the list
# print(means_of_transport[:3])


# # 7. Print the last means of transport in the list
# print(means_of_transport[-1])


# means_of_transport = ["plane", "ship", "car", "train"]
# print("before : ", means_of_transport)
# # means_of_transport[1] = "boat"
# # means_of_transport[1:2] = ["canoe", "boat"]
# # means_of_transport[1:3] = ["boat"]
# print("after  : ", means_of_transport)


# means_of_transport = ["plane", "ship", "car", "train"]
# print(len(means_of_transport))
# print(type(means_of_transport))



# odd_numbers = [9, 13, 53, 97]
# print(odd_numbers)
# print(odd_numbers[3])

# people = ["Daniel", "James", "Olaitan", "Janet", "Winnie"]
# are_happy = [False, True, True, False, True]

# means_of_transport = ["plane", False, "ship", 12, "car", "train", None, 78.9, True]
# print(means_of_transport)


# my_tuple = 1, 9, 78
# my_list = list(my_tuple)
# print(my_list)
# ==================================INTRO=============================================================



# ==================================EXTENDS=============================================================
# disciples_of_jesus = ["Peter", "Judas", "John"]
# other_disciples =  ["James", "Matthew", "Mark"]
# # other_disciples =  "James", "Matthew", "Mark"
# # other_disciples =  "James"

# print("before: ", disciples_of_jesus)
# # disciples_of_jesus.append(["James", "Matthew", "Mark"])
# # others = "James", "Matthew", "Mark"
# # disciples_of_jesus.append(others)
# # name = "Jane"
# # name.lower()
# # print(name)
# result = disciples_of_jesus.extend(other_disciples)
# print("result: ", result)
# print("after:  ", disciples_of_jesus)
# ==================================EXTENDS=============================================================



# ==================================REMOVE FROM A LIST=============================================================
# Method 1 - .remove()
# disciples = ['Peter', 'Judas', 'John', 'James', 'Matthew', 'Mark']
# print("before:  ", disciples)
# disciples.remove("Judas")
# print("after:   ", disciples)


# Method 2 - del keyword
# disciples = ['Peter', 'Judas', 'John', 'James', 'Matthew', 'Mark']
# print("before:  ", disciples)
# # del disciples[1]
# # del disciples[1:3]
# # del disciples[100]
# # del disciples

# print("after:   ", disciples)


# Method 3 - .pop() method
# disciples = ['Peter', 'Judas', 'John', 'James', 'Matthew', 'Mark']
# print("before:  ", disciples)
# disciples.pop(-2)
# popped_disciple = disciples.pop()
# disciples.pop(100)
# print("popped_disciple:", popped_disciple)
# print("after:   ", disciples)
# ==================================REMOVE FROM A LIST=============================================================



# ==================================CLEAR A LIST=============================================================
# Method 1 - .clear()
# disciples = ['Peter', 'Judas', 'John', 'James', 'Matthew', 'Mark']
# print("before:  ", disciples)
# print("id before:  ", id(disciples))

# disciples.clear()
# print("after:   ", disciples)
# print("id after :  ", id(disciples))


# Method 2 - overwrite with empty list
# disciples = ['Peter', 'Judas', 'John', 'James', 'Matthew', 'Mark']
# print("before:  ", disciples)
# print("id before:  ", id(disciples))
# disciples = []
# print("after:   ", disciples)
# print("id after :  ", id(disciples))
# ==================================CLEAR A LIST=============================================================


# ==================================SORT A LIST=============================================================
# favorite_players = ["Modric", "Mbappe", "Haaland", "Rashford", "Osimhen"]
# print("before:  ", favorite_players)
# # favorite_players.sort()
# favorite_players.sort(key=str.lower, reverse=True)
# print("after:   ", favorite_players)

# numbers = [10, 23, 1, 78]
# print("before:  ", numbers)
# numbers.sort()
# print("after:   ", numbers)

# favorite_players = ["Modric", "Mbappe", "haaland", "Rashford", "osimhen"]
# print("before:  ", favorite_players)
# favorite_players.sort()  # case-sensitive
# favorite_players.sort(key=str.lower)  # case-insensitive
# print("after:   ", favorite_players)
# ==================================SORT A LIST=============================================================


# ==================================REVERSE A LIST=============================================================
# Method 1 - .reverse()
# favorite_players = ["Modric", "Mbappe", "haaland", "Rashford", "osimhen"]
# print("before:  ", favorite_players)
# favorite_players.reverse()
# print("after:   ", favorite_players)


# Method 2 - [::-1]
# favorite_players = ["Modric", "Mbappe", "haaland", "Rashford", "osimhen"]
# print("before:  ", favorite_players)
# favorite_players = favorite_players[::-1]
# print("after:   ", favorite_players)

# Method 3 - use the reversed() function
# favorite_players = ["Modric", "Mbappe", "haaland", "Rashford", "osimhen"]
# print("before:  ", favorite_players)
# favorite_players = list(reversed(favorite_players))
# print("after:   ", favorite_players)

# action = "jump"
# action = tuple(reversed(action))
# action = "".join(action)
# print(action)
# ==================================REVERSE A LIST=============================================================



# ==================================COPY A LIST=============================================================

# Method 1 - .copy()
# fruits = ["apple", "banana", "cherry", "mango", "watermelon"]
# print("fruits     :  ", fruits)
# fruits_copy = fruits.copy()
# print("fruits copy:  ", fruits_copy)


# Method 2 - copy.copy() and copy.deepcopy()
# nested_list = [["Alice", "Bob"], ["Jane", "John"]]
# print("nested_list:  ", nested_list)
# nested_list_copy = nested_list.copy()
# nested_list_copy[1].append("James")
# print("nested_list:  ", nested_list)


# import copy
# nested_list = [["Alice", "Bob"], ["Jane", "John"]]
# print("nested_list     :  ", nested_list)
# nested_list_copy = copy.deepcopy(nested_list)
# nested_list_copy[1].append("James")
# print("nested_list:  ", nested_list)
# ==================================COPY A LIST=============================================================



# ==================================JOIN LISTS=============================================================

# # Method 1 - .extend()
# sqi_branches = ["Ogbomoso", "Abeokuta", "Osogbo"]
# ibadan_branches = ["Dugbe", "Iwo road", "Challenge"]

# sqi_branches.extend(ibadan_branches)
# print(sqi_branches)


# Method 2 - list concatenation
# sqi_branches = ["Ogbomoso", "Abeokuta", "Osogbo"]
# ibadan_branches = ["Dugbe", "Iwo road", "Challenge"]
# all_branches = sqi_branches + ibadan_branches
# print(all_branches)
# ==================================JOIN LISTS=============================================================


# ==================================NESTED LISTS=============================================================
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])
# print(matrix[1][-1])
# print(matrix[-3][-2])
# matrix[2][0] = 100
# print(matrix)
# print(matrix[1][0] + matrix[1][2])



# table = [
#     ["name", "age", "gender", "department", "branch", "is_student", "is_instructor"],
#     ["Daniel", 78, "M", "Software Engineering", "Dugbe", True, True],
#     ["Olaitan", 28, "M", "Data Science", "Dugbe", True, False],
#     ["Winifred", 29, "F", "Data Science", "Dugbe", False, True]
# ]

# # print(table[2][3][5:])
# # print(table[3])
# # print(table[1][2])
# # It is True that Olaitan is a student of Data Science
# olaitan = table[2]
# print(f"It is {olaitan[-2]} that {olaitan[0]} is a student of {olaitan[3]}")




# ==================================NESTED LISTS=============================================================



# ==================================ASSIGNMENT CORRECTION=============================================================
# Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".

# grades = ["A", "B", "C", "D"]
# # ["A", "X"]
# grades[1:] = ["X"]
# print(grades)


# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.

# import string
# alphabets = list(string.ascii_lowercase)
# print(alphabets)
# print(alphabets[-3:])


# 26. Access and print the second subject of the first person in the list.
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]

# print(data[0][2][1])

#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]

# print(records[1][-1][0])

#  28.	Get the first e in Ayo’s gender and Get Ben’s age.
# group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]

# print(group[0][1][0][1])
# print(group[1][-1][-1])

#  29.	Get the l in Nina’s gender and Get Tobi’s age
# 	records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
#  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
# print(robot_grid[-1][1][0][-1][1:3])
# print(robot_grid[0][1][1][0])

# "oo"

#  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]

# print(playlist[0][-1][0].split(" ")[1])
# print(playlist[0][-1][0][-4:])
# print(playlist[0][-1][-1])

#  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
# print(animals[1][-1][0][5])
# print(animals[-1][-1][0][0])

# ==================================ASSIGNMENT CORRECTION=============================================================