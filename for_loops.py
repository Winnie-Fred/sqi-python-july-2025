# item = ["board", "screen", "shoe", "bag"]

# for something in item:
#     print(something)



# items = ["board", "screen", "shoe", "bag"]
# for item in items:
#     print(item)



# items = ["board", "screen", "shoe", "bag"]

# i = 0

# while i < len(items):
#     item = items[i]
#     print(item)
#     i += 1



# birds = ["hen", "duck", "eagle", "falcon", "vulture"]
# for _ in birds:
#     # print(birds)
#     print("hello")


# birds = ["hen", "duck", "eagle", "falcon", "vulture"]
# for bird in birds:
#     # print(birds)
#     print(bird)


# name = "Olaitan"

# for char in name:
#     print(char)



# 1. Create a tuple called `colors` containing 6 of your favorite colors.
# Loop through the tuple and print each color using a for loop

# 2. Create a tuple called `colors` containing 6 of your favorite colors.

# Expected Output:
# I love green
# I love red
# I love black
# I love yellow
# I love white
# I love purple


# colors = {"red": 4, "black": 6, "white": 2, "yellow": 8, "purple": 3}

# print(colors.items())


# for color, num in colors.items():
#     print(color)
#     print(num)


# scores = {"Olaitan": 99, "Daniel": 50, "Winnie": 45}
# for student, score in scores.items():
#     print(f"{student} got {score}")


states_and_capitals = {"Ogun": "Abeokuta", "Delta": "Asaba", "Anambra": "Awka"}

# The capital of Ogun is Abeokuta
# The capital of Delta is Asaba
# The capital of Anambra is Awka


# actions = ["run", "sleep", "skip", "stop", "wake"]

# for action in actions:
#     if action == "stop":
#         break
#     print(action)

# actions = ["run", "sleep", "skip", "stop", "wake"]

# for action in actions:
#     if action != "skip":
#         print(action)


# actions = ["run", "sleep", "skip", "stop", "wake"]

# for action in actions:
#     if action == "skip":
#         continue
#     print(action)


# for action in ["run", "sleep", "skip", "stop", "wake"]:
#     if action == "skip":
#         continue
#     print(action)


# print(list(range(1, 78)))

# for num in range(1, 79):
#     print(num)

# for num in range(0, 79, 2):
#     print(num)

# for num in range(79, 0, -1):
#     print(num)



# sentence = "I am learning python at SQI"

# # I Am LeArNiNg PyThOn At SqI

# actions = ["run", "sleep", "skip", "stop", "wake"]
# print(list(enumerate(actions, start=100)))

# for idx, action in enumerate(actions):
#     print(idx)
#     print(action)


# actions = ["run", "sleep", "skip", "stop", "wake"]

# 1. run
# 2. sleep
# 3. skip
# 4. stop
# 5. wake 

# sentence = "I am learning python at SQI"
# words = sentence.split()
# processed_words = []


# for word in words:
#     processed_word = ""

#     for idx, char in enumerate(word):
#         if idx % 2 == 0:
#             processed_word += char.upper()
#         else:
#             processed_word += char.lower()
#     processed_words.append(processed_word)

# processed_words = " ".join(processed_words)
# print(processed_words)


# sentence = "I am learning python at SQI"
# words = sentence.split()
# processed_words = []


# for word in words:
#     processed_word = ""

#     upper = True
#     for idx, char in enumerate(word):
#         if upper:
#             processed_word += char.upper()
#         else:
#             processed_word += char.lower()
#         upper = not upper
#     processed_words.append(processed_word)

# processed_words = " ".join(processed_words)
# print(processed_words)



# sentence = "I am learning python at SQI"
# words = sentence.split()
# processed_words = []


# for word in words:
#     processed_word = ""

#     upper = True
#     # for idx, char in enumerate(word):
#     for idx in range(len(word)):
#         char = word[idx]
#         if upper:
#             processed_word += char.upper()
#         else:
#             processed_word += char.lower()
#         upper = not upper
#     processed_words.append(processed_word)

# processed_words = " ".join(processed_words)
# print(processed_words)



# actions = ["run", "sleep", "skip", "stop", "wake"]

# for idx in range(len(actions)):
#     action = actions[idx]
#     print(f"{idx+1}. {action}")


# actions = ["run", "sleep", "skip", "stop", "wake"]
# actions = []
# for action in actions:
#     print(action)
# else:
#     print('Finished running')


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")


# adjectives = ["fierce", "majestic", "playful", "happy", "Sad"]
# animals = ["lion", "eagle", "dolphin"]

# print(list(zip(adjectives, animals)))


# for adjective, animal in zip(adjectives, animals):
#     print(f"{adjective} {animal}")



# adjectives = ["fierce", "majestic", "playful", "sad", "happy"]
# animals = ["lion", "eagle", "dolphin"]

# i = 0

# while i < len(adjective):
#     animal = animals[i]
#     adjective = adjectives[i]
#     print(f"{adjective} {animal}")
#     i += 1



# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60



# =====================================LIST COMPREHENSION==========================================


# numbers_in_words = ["four", "forty-five", "twenty", "nineteen"]

# numbers_in_words_copy = []

# for number in numbers_in_words:
#     numbers_in_words_copy.append(number.upper())

# print(numbers_in_words_copy)




# numbers_in_words = ["four", "forty-five", "twenty", "nineteen"]
# numbers_in_words_copy = [number.upper() for number in numbers_in_words]
# print(numbers_in_words_copy)

# places_in_lag = ["Lekki", "Magodo", "Ojuelegba", "Ojota", "Mile 2", "Oshodi"]
# lowercase_places_in_lag = [place.lower() for place in places_in_lag]
# print(lowercase_places_in_lag)


# places_in_lag = ["Lekki", "Magodo", "Ojuelegba", "Ojota", "Mile 2", "Oshodi"]
# # [False, False, True, True, False, True]
# vowels = ("a", "e", "i", "o", "u")
# starts_with_vowel = [place.lower()[0] in vowels for place in places_in_lag]
# print(starts_with_vowel)
# starts_with_vowel = [place.lower().startswith(vowels) for place in places_in_lag]
# print(starts_with_vowel)


# bodies_of_water = ("stream", "river", "ocean", "pond", "pool", "spring", "dam", "lake")
# [1, 1, 1, 0, 0, 0, 0, 1]

# name = "Winnie"
# name.count("n")
# 

# string = input("Enter the string: ").lower()  # hippopotamus
# substring = input("Enter the substring you want to count in the string: ").lower()  # p

# Don't use .count()

# occurences = 0

# i = 0

# while i < len(string):
#     char = string[i]

#     if char == substring:
#         occurences += 1

#     i += 1

# print(occurences)


# string = input("Enter the string: ").lower()  # hippopotamus
# substring = input("Enter the substring you want to count in the string: ").lower()  # pp
# count = 0

# while True:
#     substr_pos = string.find(substring)
#     if substr_pos != -1:
#         count += 1
#     else:
#         break
#     string = string[substr_pos+len(substring):]


# print(count)


# string = input("Enter the string: ").lower()  # hippopotamus
# substring = input("Enter the substring you want to count in the string: ").lower()  # pp

# # mississippi
# # ss

# i = 0
# count = 0
# while i < len(string):
#     _slice = string[i:i+len(substring)]
#     if _slice == substring:
#         count += 1
#     i += 1

# print(count)



# numbers = [2, 9, 12, 78, 234, 1]
# even_nos = []
# for num in numbers:
#     if num % 2 == 0:
#         even_nos.append(num)

# print(even_nos)

# numbers = [2, 9, 12, 78, 234, 1]

# even_nos = [num for num in numbers if num % 2 == 0]

# print(even_nos)


# places_in_lag = ["Lekki", "Magodo", "Ojuelegba", "Ojota", "Mile 2", "Oshodi"]
# ["Ojuelegba", "Ojota", "Oshodi"]


# Get only the nums divisible by 5 from 17 to 90

# nums_div_by_5 = [num for num in range(17, 91) if num % 5 == 0]
# print(nums_div_by_5)


# 1. Create a list of the lengths of the words
# Input: ["apple", "banana", "kiwi", "pear"]
# Expected Output: [5, 6, 4, 4]
words = ["apple", "banana", "kiwi", "pear"]
 

# 3. Create a list of the words that start with the letter 's'
# Input: ["sun", "cloud", "sky", "moon", "star"]
# Expected Output: ["sun", "sky", "star"]
weather_terms = ["sun", "cloud", "sky", "moon", "star"]


# 4. Create a list of each number doubled
# Input: [3, 6, 9, 12]
# Expected Output: [6, 12, 18, 24]
nums = [3, 6, 9, 12]



# 6. Create a list of words that have more than 3 letters
# Input: ["go", "on", "ride", "stop", "yes"]
# Expected Output: ["ride", "stop"]
commands = ["go", "on", "ride", "stop", "yes"]


# Assignment
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

# =====================================LIST COMPREHENSION==========================================


# =====================================ASSIGNMENT CORRECTION==========================================
# Time to test your knowledge
# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. 
# Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = input("Enter comma-separated numbers: ").split(",")
# numbers = [int(num) for num in numbers]
# unique_nums = []

# for num in numbers:
#     if num not in unique_nums:
#         unique_nums.append(num)

# print(unique_nums)


# 6. Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. 
# Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# n = int(input("Enter the length of the fubinacci sequence: "))
# fibonacci = [0, 1]

# i = 0

# while i < n - 2:
#     result = fibonacci[i] + fibonacci[i+1]
#     fibonacci.append(result)
#     i += 1

# print(fibonacci) 

# 8. Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Enter the value of n: "))

# i = 2
# sum_of_even = 0
# while i <= n:
#     sum_of_even += i
#     i += 2

# print(sum_of_even)

# n = int(input("Enter the value of n: "))
# sum_even_nos = sum([num for num in range(2, n+1) if num % 2 == 0])
# print(sum_even_nos)

# n = int(input("Enter the value of n: "))
# sum_even_nos = sum([num for num in range(2, n+1, 2)])
# print(sum_even_nos)


# 10. Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)

# n = int(input("Enter the value of n: "))
# i = 1
# result = 0
# while i <= n:
#     # result += i ** 2
#     result += i * i
#     i += 1

# print(result)

# 12. Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# text = input("Enter some text: ").strip()
# words = text.split()

# no_of_words = 0

# for word in words:
#     no_of_words += 1

# print(no_of_words)


# 20.	Given two lists of numbers of the same length, print the indices and values
# of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
# 'Index 1: 8 != 3',
# 'Index 3: 7 != 9',
# 'Index 5: 4 != 0',
# ]

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]
# result = []
# for idx, (list1_item, list2_item) in enumerate(zip(list1, list2)):
#     if list1_item != list2_item:
#         result.append(f'Index {idx}: {list1_item} != {list2_item}')

# print(result)

# =====================================ASSIGNMENT CORRECTION==========================================



# =====================================DICTIONARY COMPREHENSION==========================================
# animals = ["dog", "cat", "lion", "tiger"]
# # {"dog": 3, "cat": 3, "lion": 4, "tiger": 5}

# len_animals = {}
# for animal in animals:
#     len_animals[animal] = len(animal)

# print(len_animals)


# # animals = ["dog", "cat", "lion", "tiger"]
# len_animals = {animal: len(animal) for animal in animals}
# print(len_animals)

# animals = ["dog", "cat", "eagle", "lion", "antelope", "tiger"]
# {"dog": False, "cat": False, "eagle": True, "lion": False, "antelope": True, "tiger": False}



# =====================================DICTIONARY COMPREHENSION==========================================


# =====================================SET COMPREHENSION==========================================
# animals = ["dog", "cat", "lion", "tiger"]
# len_animals = {len(animal) for animal in animals}  # set comprehension
# print(len_animals)
# =====================================SET COMPREHENSION==========================================


# =====================================GENERATORS==========================================
# animals = ["dog", "cat", "lion", "eagle", "tiger", "antelope"]
# animals = ["eagle", "antelope"]
# vowels = ("a", "e", "i", "o", "u")
# starts_with_vowel = (animal.lower().startswith(vowels) for animal in animals)
# starts_with_vowel = [animal.lower().startswith(vowels) for animal in animals]
# print(all(starts_with_vowel))
# print(any(starts_with_vowel))

# starts_with_vowel = all(animal.lower().startswith(vowels) for animal in animals)
# starts_with_vowel = any(animal.lower().startswith(vowels) for animal in animals)
# print(starts_with_vowel)


# print(all([True, True, False]))
# print(any([True, True, False]))


# 1. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
values = [5, 12, 3, 18, 7]


# 2. Are all the words are made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]


# 3. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]


# 4. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]

# 5. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

# =====================================GENERATORS==========================================


# =====================================ASSIGNMENT==========================================
# 1. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]
all_odd = all(num % 2 != 0 for num in values)
print(all_odd)

# 2. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]


# 3. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]


# 4. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
temperatures = [12, 7, 3, -1, 5]

# 5. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]


# 6. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]


# 7. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
# numbers = [5, -2, 3, 0, 8]
# numbers = [5, 4, 3, 3, 8]
# print(any(num < 0 for num in numbers))


# 8. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]


# 9. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]



# 10. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]
# =====================================ASSIGNMENT==========================================


