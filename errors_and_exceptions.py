# print("first line")
# print(6 / 0)

# print("first line")
# print("first line)
# print(6 / 0)




# try:
#     num1 = int(input("Enter the value of num1: "))
#     num2 = int(input("Enter the value of num2: "))
#     result = num1 / num2
#     del result
#     print(result)
# # except:
# except ValueError as e:
#     print("num1 and num2 must be integers:", e)
# except ZeroDivisionError as e:
#     print("num2 must be an integer:", e)
# except Exception as e:
#     print("Something went wrong", e)


# Ask the user for their age
# if the user enters a non-integer, tell them "age must be an integer", and keep asking till they enter
# a valid age
# if the age is negative, print "age must not be negative", and keep asking till they enter a
# valid age
# if the age is a positive integer, then print "You were born in {birth_year}".

# try:
#     num1 = int(input("Enter the value of num1: "))
#     num2 = int(input("Enter the value of num2: "))
#     result = num1 / num2
# # except:
# except ValueError as e:
#     print("num1 and num2 must be integers:", e)
# except ZeroDivisionError as e:
#     print("num2 must be an integer:", e)
# except Exception as e:
#     print("Something went wrong", e)
# else:
#     print(f"The result is: {result}")


# try:
#     num1 = int(input("Enter the value of num1: "))
#     num2 = int(input("Enter the value of num2: "))
#     result = num1 / num2
#     del result
# # except:
# except ValueError as e:
#     print("num1 and num2 must be integers:", e)
# except ZeroDivisionError as e:
#     print("num2 must be an integer:", e)
# except Exception as e:
#     print("Something went wrong", e)
# else:
#     print(f"The result is: {result}")


# class NegativeOrZeroAgeError(Exception):
#     def __init__(self, age):
#         self.message = f"Age entered: {age}. Age must be greater than zero."
#         super().__init__(self.message)


# from datetime import datetime
# current_year = datetime.now().year


# def calculate_birth_year():
#     while True:
#         try:
#             age = int(input("How old are you now? "))
#         except ValueError as e:
#             print(f"Age must be an integer: {e}")
#             continue
#         else:
#             if age < 1:
#                 # raise ValueError("Age must be 1 or greater")
#                 raise NegativeOrZeroAgeError(age)
#             print(f"You were born in {current_year - age}")
#             break


# try:
#     calculate_birth_year()
# except NegativeOrZeroAgeError as e:
#     print(e)


# from datetime import datetime
# current_year = datetime.now().year


# def calculate_birth_year():
#     try:
#         age = int(input("How old are you now? "))
#     except ValueError as e:
#         print(f"Age must be an integer: {e}")
#     else:
#         if age < 1:
#             print("Age must be greater than zero")
#         else:
#             print(f"You were born in {current_year - age}")
#             return
#     finally:
#         print("This will always run")

# calculate_birth_year()


# def add_two_nums(num1, num2):
#     try:
#         result = int(num1) + int(num2)
#     except TypeError as e:
#         print(f"num1 and num2 must be integers or strings containing integers: {e}")
#         return
#     except ValueError as e:
#         print(f"num1 and num2 must be convertible to ints: {e}")
#         return
#     return result


# print(add_two_nums(4, 6))
# print(add_two_nums(4, "6"))
# print(add_two_nums(4, "6ebhfcjnmkx,l"))
# print(add_two_nums(4, [4, 9, 1]))


# def add_two_nums():
#     try:
#         num1 = input("Enter num1:")
#         num2 = input("Enter num1:")
#         result = int(num1) + int(num2)
#     except TypeError as e:
#         print(f"num1 and num2 must be integers or strings containing integers: {e}")
#         return
#     except ValueError as e:
#         print(f"num1 and num2 must be convertible to ints: {e}")
#         return
#     return result

# try:
#     print(add_two_nums())
# except KeyboardInterrupt as e:
#     print("\nProgram interrupted")




# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# class NegativeNumberError(Exception):
#     def __init__(self, num):
#         super().__init__(f"{num} is negative")


# def check_positive(number: int):
#     if number < 0:
#         raise NegativeNumberError(number)

#     return f"{number} is positive"

# try:
#     result = check_positive(-6)
# except NegativeNumberError as e:
#     print(e)
# else:
#     print(result)
