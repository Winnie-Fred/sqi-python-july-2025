"""
This is the functions file for SQI Python July 2025 Cohort.
"""
# def greet():
#     # print("Good afternoon, SQI July Python Gurus")
#     return "Good afternoon, SQI July Python Gurus"
#     print("inside function")


# print(greet())



# def greet():
#     print('Hello World!')

# greet()
# print('Outside function')

# Output:
# Hello World
# Outside function




# print("Lorem ipsum dolor")  # 1
# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8


# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()
# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12



# def add_two_nums(num1, num2):
#     return num1 + num2

# print(add_two_nums(6, 9))  # 15


# result = add_two_nums(6, 10)
# print(result)  # 16


# Write a function called multiply_3_nums that takes in num1, num2 and num3 and returns the result of their product
# Store the result in a variable and print it




# Write a function is_even(num) that takes in a number that return a boolean True if the number is even, otherwise, return False


# # BEGINNER
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(7))
# print(is_even(8))


# # INTERMEDIATE
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# print(is_even(7))
# print(is_even(8))



# # ADVANCED
# def is_even(num):
#     return num % 2 == 0

# print(is_even(7))
# print(is_even(8))


# def is_even(num):
#     return num % 2 == 0

# print(is_even(num=7))
# print(is_even(num=8))


# 48 - 57
# Optional - if char is more than one char after stripping, return None
# def char_is_digit(char: str):
# def _char_is_digit(char: str):
#     char = char.strip()
#     if len(char) > 1:
#         raise ValueError("char must be a single character")
#     return 48 <= ord(char) <= 57

# # print(char_is_digit("8"))  # True
# # # print(char_is_digit("ygdybhn"))  # True
# # print(char_is_digit("a"))  # False


# def string_contains_digit(string):
#     return any(_char_is_digit(char) for char in string)

# print(string_contains_digit("ygdybhn"))

# def string_all_digits(string):  # parameter
#     return all(_char_is_digit(char) for char in string)

# print(string_all_digits("ygdybhn"))  # argument
# print(string_all_digits("12345"))  # argument

# chars_all_digits = string_all_digits("good5678")

# print(chars_all_digits("good789"))


# print()
# print("hello")


# print = "hello"
# print(print)


# def greet_everyone(names_and_emojis: dict[str, str]):
#     for name, emoji in names_and_emojis.items():
#         print(f"{name} says Hi {emoji}")


# print(greet_everyone({"Daniel": "😴", "Olaitan": "😈", "Winnie": "😆"}))

# Daniel says Hi 😴
# Olaitan says Hi 😈
# Winnie says Hi 😆


# def greet(time_of_day="morning", name="Anonymous",):
#     return f"Good {time_of_day}, {name}"

# print(greet())

# 1. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     pass

# print(lesser_of_two_evens(5, 6))  # 6
# print(lesser_of_two_evens(5, 7))  # 7
# print(lesser_of_two_evens(2, 8))  # 2

# # 2. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.


# def is_alliteration(two_word_string):
#     pass


# is_alliteration("Levelheaded llama") # True
# is_alliteration("Crazy Kangaroo") # False


# 3. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name: str):
#     # return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
#     return name[0:3].capitalize() + name[3:].capitalize()

# print(old_macdonald('macdonald'))  # MacDonald
# print(old_macdonald('macmahon'))  # MacMahon

# *args and **kwargs


# def add_all_nums(nums: list[int]):
#     return sum(nums)

# print(add_all_nums([2, 39, 10, 2903, 290, 123, 123]))


# def add_all_nums(*nums):
#     return sum(nums)

# print(add_all_nums(2, 39, 10, 2903, 290, 123, 123))



# def say_hi_to_everyone(*everyone):
#     for name in everyone:
#         print(f"Hi {name} 🙋‍♀️")

# say_hi_to_everyone("Olaitan", "Dan", "Winnie")


# args - arbitrary arguments - 0, 1 or more
# kwargs - arbitrary keyword arguments - 0, 1 or more

# def translate_to_yoruba(**dictionary):
#     for english, yoruba in dictionary.items():
#         print(f"{english} ➡️  {yoruba}")


# translate_to_yoruba(book="iwe", shoe="bata", broom="igbale", male="okunrin")
# dictionary = {
#     "book": "iwe",
#     "shoe": "bata",
#     "broom": "igbale",
#     "male": "okunrin",
#     "sit down": "joko"
# }
# translate_to_yoruba(**dictionary)


# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}"

# print(greet("Winnie", "morning"))
# print(greet(time_of_day="morning", name="Winnie"))


# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call

# print(power(2, 3))  # Output: 8

# 2 * power(2, 2)

# 2 * 2 * power(2, 1)

# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1


# print(power(2, 1000))


# name = "Winnie"

# def my_func():
#     """
#     This is my function
#     """
#     global name
#     name = "Olaitan"
#     print("Inside function:", name)


# my_func()
# print("Outside function:", name)



# def add(a: int, b: int):
#     """
#     Add two numbers and return the result.
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.

#     Returns:
#     int, float: The sum of the two numbers.
#     """
#     return a + b




# ---------------------------------*args and **kwargs assignment---------------------------------
# 1. Create a function called count_words(*words) that returns the number of words passed in.

# # Test Data:
# print(count_words("apple", "banana", "cherry"))
# print(count_words("one", "two"))

# Expected Output:
# 3
# 2


# 2. Create a function called get_long_words(*words) that returns only the words with more than 4 letters.


# # Test Data:
# print(get_long_words("tree", "watermelon", "hat", "giraffe"))
# print(get_long_words("sun", "elephant", "sky", "pen"))

# Expected Output:
# ['watermelon', 'giraffe']
# ['elephant']


# 3. Create a function called sum_all(*numbers) that returns the sum of all the numbers.

# # Test Data:
# print(sum_all(2, 3, 4))
# print(sum_all(1, 5, 10, 2))

# Expected Output:
# 24
# 100


# 4. Create a function called multiply_all(*numbers) that returns the product of all the numbers.

# # Test Data:
# print(multiply_all(2, 3, 4))
# print(multiply_all(1, 5, 10, 2))

# Expected Output:
# 24
# 100

# 5. Create a function called filter_out_odd(num1, num2, *numbers) that returns a list of only the even numbers from all the arguments passed in.


# print(filter_out_odd(9, 100, 34, 89, 12))  # [100, 34, 12]
# print(filter_out_odd(12, 13))  # [12]
# print(filter_out_odd(2, 3, 9, 0))  # [2, 0]

# 6. Create a function called count_items that returns the total number of values passed in (both args and kwargs).


# Test Data:
# print(count_items("apple", "banana", fruit="orange", color="red"))
# print(count_items(1, 2, 3, name="Tom"))


# # Expected Output:
# # 4
# # 4


# 7. Create a function called len_all_items that returns the length of all the values passed in (both args and kwargs).


# # Test Data:
# print(len_all_items("apple", "banana", fruit="orange", color="red"))
# print(len_all_items("hello", "you", food="yam", ingredient="pepper"))


# # Expected Output:
# # 20
# # 17

# ---------------------------------*args and **kwargs assignment---------------------------------


def greet(name, time_of_day):
    return f"Good {time_of_day}, {name}"

# print(greet("Winnie", "morning"))
# name = "Winnie"
# time_of_day = "morning"
# print(greet(name, time_of_day))
# my_name = "Winnie"
# time_of_the_day = "morning"
# # print(greet(my_name, time_of_the_day))  # *args
# print(greet(name=my_name, time_of_day=time_of_the_day))  # **kwargs



# def winnie_sum(*numbers):
#     print(type(numbers))
#     print(numbers)
#     return sum(numbers)


# print(winnie_sum(2, 90, 67, 12, 79))

# print("Daniel", "is", "learning", "Python", "Python", "is", "amazing")
# print("Daniel")


# nums1 = [1, 2]
# nums2 = [3, 4]

# nums = [*nums1, *nums2]
# print(nums)



# def sum_numbers(num1, num2, *numbers):
#     numbers = [num1, num2, *numbers]
#     return sum(numbers)

# print(sum_numbers(1))


# def show_grade(**grades):
#     print(grades)
#     print(type(grades))

#     for grade, score in grades.items():
#         print(f"{score} -> {grade}")

# show_grade(a=75, e=40, f=12)


# show_grade(a=75, e=40, f=12)
# grades = {'a': 75, 'e': 40, 'f': 12}
# show_grade(**grades)


# def sqi_python_july_2025_print(*args, separator="; ", **kwargs):
#     values = kwargs.values()
#     print(*args, *values, sep=separator)

# # sqi_python_july_2025_print("-", 12, 3, 89, "hello", winnie=23, olaitan=29, daniel=90)
# sqi_python_july_2025_print(12, 3, 89, "hello", separator="[]", winnie=23, olaitan=29, daniel=90)



# def log_message(*args, **kwargs):
#     message_part_1 = " ".join(args)
#     message_part_2 = []
#     for key, value in kwargs.items():
#         message_part_2.append(f"{key}={value}")
#     message_part_2 = ", ".join(message_part_2)
#     if not kwargs:
#         return f"[LOG] {message_part_1}"
#     return f"[LOG] {message_part_1} | {message_part_2}"


# print(log_message("User", "logged", "in", user="winnie", role="admin", time="12:30"))

# # Expected Output
# # [LOG] User logged in | user=winnie, role=admin, time=12:30

# print(log_message("System", "restarted"))
# # Expected Output
# # [LOG] System restarted



# ---------------------------------VARIABLE SCOPE---------------------------------



def greet():
    # global name
    # name = "Winnie"
    age = 12
    print(age)
    return f"inside function: {name}"

name = "Olaitan"
print(greet())
print(f"Outside function: {name}")

# ---------------------------------VARIABLE SCOPE---------------------------------
