# def is_nigerian_phone_no(phone_no: str):
#     code = ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O']
#     if len(phone_no) != len(code):
#         return False
    
#     for char in phone_no:
#         code_digit = code[0]
#         if code_digit == 'O' and char.isdigit():
#             code.pop(0)
#         elif code_digit == 'X' and char.isspace():
#             code.pop(0)
#     return not code

# with open("data.txt", "r") as f:
#     contents = f.read()

# nigerian_phone_nos = []
# i = 0
# while i < len(contents):
#     window = contents[i:i+13]
#     if is_nigerian_phone_no(window):
#         nigerian_phone_nos.append(window)
#     i += 1        

# print("Nigerian phone numbers: ")
# print(nigerian_phone_nos)
# print(extract_numbers(text))




# with open("data.txt", "r") as f:
#     text = f.read()

# def extract_numbers(text):
#     numbers = []
#     tokens = text.split()
    
#     for i in range(len(tokens)):
#         # Join 3 consecutive tokens, in case numbers are split with spaces
#         possible = "".join(tokens[i:i+3])
#         print("possible:", possible)
#         clean = "".join(ch for ch in possible if ch.isdigit())
#         print("clean:  ", clean)

#         if clean.startswith(("080", "081", "070", "090")) and len(clean) == 11:
#             numbers.append(clean)
    
#     return list(set(numbers))  # remove duplicates if any


# print(extract_numbers(text))

# import re
# Example 1: Simple match
# pattern = r"word\b"
# text = "A word in a sentence."
# match = re.search(pattern, text)

# if match is not None:
#     print("Match found:", match.group())  # Match found: word
# else:
#     print("No match found")

# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']


# Example 3: Replace text
# pattern = r"\s+"
# text = "This   is a \ttest."
# new_text = re.sub(pattern, " ", text)
# print("Original text:", text)  # Replaced text: This is a test.
# print("Replaced text:", new_text)  # Replaced text: This is a test.


# text = "\tWinnie"
# print(text)

# import re
# # Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "Contact us at support@example.com for more info. Or use olaitan@gmail.com"
# match = re.search(pattern, text)
# print(match)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com


# import re
# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']

# import re
# # Example 3: Validate a phone number (US format)
# pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
# phone_number = "(123) 456-7890"
# if re.match(pattern, phone_number):
#     print("Valid phone number")  # Valid phone number
# else:
#     print("Invalid phone number")


import re
with open("data.txt", "r") as f:
    text = f.read()


pattern = r"\d{4} \d{3} \d{4}"
phone_numbers = re.findall(pattern, text)
print(phone_numbers)