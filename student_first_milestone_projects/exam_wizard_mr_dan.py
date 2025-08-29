theory = [
    {
        "question": "What is a noun?",
        "keyword":{
            "name": 2,
            "things": 1
        },
        "question": "What is a verb?",
        "keyword":{
            "action": 2,
            "word": 1
        },
        "question": "What is a snake?",
        "keyword":{
            "crawling": 2,
            "animal": 1
        },
        "question": "Explain what is the mouth used for",
        "keyword":{
            "talikg": 2,
            "chewing": 1
        },
    }
]

print("Welcome to Examinar")
header = """
#########################
#      EXAM SCHOOL      #   
#########################
"""
print(header)
score = 0
idx = 0
while idx < len(theory):
    