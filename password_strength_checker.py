# password = "p@sSw😊rd"
# password = "p@sSw0rd"
# password = "password"


# # Is at least 8 characters long.

# has_at_least_8_chars = len(password) >= 8

# # Contains both uppercase and lowercase characters.
# has_upper = any(char.isupper() for char in password)

# has_lower = any(char.islower() for char in password)

# # Contains at least one digit.

# has_digit = any(char.isdigit() for char in password)

# # Contains at least one special character (e.g., !@#$%^&*()).
# has_special_char = any(char in "!@#$%^&*()" for char in password)

# # is_strong = all([has_at_least_8_chars, has_upper, has_lower, has_special_char, has_digit])
# is_strong = has_at_least_8_chars and has_upper and has_lower and has_special_char and has_digit
# print(is_strong)
# must have smiley face 😊

# has_smiley = any(char == "😊" for char in password)
# print("Has smiley:", has_smiley)



# print(password)

# def is_strong_password(password):
#     has_at_least_8_chars = len(password) >= 8
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special_char = False


#     for char in password:
#         if char.isupper():
#             has_upper = True
#         if char.islower():
#             has_lower = True
#         if char.isdigit():
#             has_digit = True
#         if char in "!@#$%^&*()":
#             has_special_char = True

#     is_strong = has_at_least_8_chars and has_upper and has_lower and has_special_char and has_digit

#     return is_strong


# password1 = "Passw0rd@"
# is_strong_password(password1)


# password2 = "StrongPassword"
# is_strong_password(password2)

# password3 = "12345678"
# is_strong_password(password3)



# def square_num(num):
#     return num ** 2

# square_num(5)
