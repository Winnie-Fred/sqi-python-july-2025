#                        Lists          Tuples                  Dictionaries                                            Sets

# Mutable                  Yes          No                          Yes                                                 Yes
# Ordered                  Yes          Yes                         Yes (in newer versions of Python)                   No
# Indexed                  Yes          Yes                         Yes (but with keys)                                 No
# Allow duplicates?        Yes          Yes                         Duplicate values but not duplicate keys             No



# empty_set = set()
# print(type(empty_set))


# my_set = {"eggs", "tomatoes", "eggs", "onions"}
# # print(type(my_set))
# print(my_set)
# print(my_set[0])


# my_set = {1, 0, True, False, True, 10, 2, 0}
# print(my_set)

# my_set = {1, 0, True, False, True, 10, 2, 0}
# print(len(my_set))


# items = {"tie", "comb", "shoe", "socks", "bag"}
# print(len(items))


# items = {"tie", "comb", "shoe", "socks", "bag"}
# print(type(items))


# items = ["tie", "comb", "shoe", "comb", "socks", "bag"]

# print(set(items))

# items = set(items)
# print(items)


# Change it to a string without the duplicates
# the order does not matter
# word = "hello"
# word = set(word)
# word = "".join(word)
# print(word)

# items = ["tie", "comb", "shoe", "comb", "socks", "bag"]
# print("bag" in items)
# print("bags" in items)


# ******************************SET METHODS******************************



# ==================================ADDING TO A SET=============================================================

# items = {"tie", "comb", "shoe", "socks", "bag"}
# items.add("cap")
# print(items)


# items = {"tie", "comb", "shoe", "socks", "bag"}
# other_clothing_items = ["shirt", "skirt"]
# even_more_clothes = ("trousers", "glasses")
# # other_clothing_items = "skirt"
# items.update(other_clothing_items)
# items.update(even_more_clothes)
# print(items)

# items = {"tie", "comb", "shoe", "socks", "bag"}
# other_clothing_items = ["shirt", "skirt"]
# even_more_clothes = ("trousers", "glasses")
# all_items = items.union(other_clothing_items).union(even_more_clothes)
# print(all_items)

# items = {"tie", "comb", "shoe", "socks", "bag"}
# other_clothing_items = {"shirt", "skirt"}
# even_more_clothes = {"trousers", "glasses"}
# all_items = items | other_clothing_items | even_more_clothes
# print(all_items)
# ==================================ADDING TO A SET=============================================================


# ==================================INTERSECTION=============================================================
# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange"}
# more_fuits = {"cherry", "soursop", "mango", "coconut"}

# fruits.intersection_update(other_fruits)
# fruits.intersection_update(more_fuits)
# print(fruits)


# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange"}
# more_fuits = {"cherry", "soursop", "coconut"}
# fruits_in_common = fruits.intersection(other_fruits).intersection(more_fuits)
# print(fruits_in_common)

# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# more_fuits = {"cherry", "apple", "soursop", "mango", "coconut"}

# fruits_in_common = fruits & other_fruits & more_fuits
# print(fruits_in_common)
# ==================================INTERSECTION=============================================================



# ==================================REMOVE FROM A SET=============================================================

# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# other_fruits.remove("pineapple")
# other_fruits.remove("cherry")  # KeyError
# print(other_fruits)


# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# other_fruits.discard("pineapple")
# other_fruits.discard("cherry")
# print(other_fruits)


# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# other_fruits.pop()
# print(other_fruits)

# import random

# other_fruits = ["pineapple", "mango", "guava", "orange", "apple"]
# random_fruit = random.choice(other_fruits)
# print(random_fruit)


# ==================================REMOVE FROM A SET=============================================================


# ==================================DIFFERENCE=============================================================
# laptop_brands = {"MacBook", "Dell", "HP", "Acer"}
# other_brands = {"Lenovo", "Acer", "Chromebook", "HP", "Asus"}

# difference = laptop_brands.difference(other_brands)
# print(difference)

# 7 - 3 = 4
# ||||


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# # set2 = ("google", "microsoft", "apple")  # TypeError
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# ==================================DIFFERENCE=============================================================


# ==================================SYMMETRIC DIFFERENCE=============================================================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# symmetric_diff = set1.symmetric_difference(set2)
# print(symmetric_diff)


# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# # banana, pineapple, guava, orange, cherry, apple, soursop, mango, coconut
# more_fuits = {"cherry", "apple", "soursop", "mango", "coconut"}
# symmetric_diff = fruits.symmetric_difference(other_fruits).symmetric_difference(more_fuits)
# print(symmetric_diff)

# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# # banana, pineapple, guava, orange, cherry, apple, soursop, mango, coconut
# more_fuits = {"cherry", "apple", "soursop", "mango", "coconut"}
# symmetric_diff = fruits ^ other_fruits ^ more_fuits
# print(symmetric_diff)


# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# fruits.symmetric_difference_update(other_fruits)
# print(fruits)

# ==================================SYMMETRIC DIFFERENCE=============================================================



# ==================================EXTRAS=============================================================

# fruits = {"apple", "mango", "banana"}
# # fruits.clear()  # modify existing set
# fruits = set()  # create a new set
# print(fruits)

# isdisjoint()
# fruits = {"apple", "mango", "banana"}
# other_fruits = {"pineapple", "mango", "guava", "orange", "apple"}
# print(not(bool(fruits.intersection(other_fruits))))
# print(fruits.isdisjoint(other_fruits))


# fruits = {"banana"}
# other_fruits = {"pineapple", "guava", "orange"}
# print(not(bool(fruits.intersection(other_fruits))))
# print(fruits.isdisjoint(other_fruits))



# set1 = {1, 2, 3, 4, 5, 6}
# # set2 = {3, 5, 2}
# # set2 = {13, 50, 27}
# set2 = {1, 2, 3, 4, 5, 6}
# # print(set2.issubset(set1))
# print(set2 <= set1)

# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {1, 2, 3, 4, 5, 6}
# print(set1.isdisjoint(set2))

# ==================================EXTRAS=============================================================