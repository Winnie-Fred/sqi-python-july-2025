questions = [
    {
        "question": "1. What is Economics?.",
        "keywords": {
            "social science": 3,
            "human behaviour": 3,
            "ends": 2,
            "scarce means": 2,
            "alternative uses": 2
        }
    },
    {
        "question": "2. What is demand?",
        "keywords": {
            "ability and willingness": 4,
            "consumer": 4,
            "at a given price": 4,
            "at a particular time": 4
        }
    },
    {
        "question": "3. Define the concept of supply.",
        "keywords": {
             "ability and willingness": 4,
            "producer": 4,
            "at a given price": 4,
            "at a particular time": 4
        }
    },
    {
        "question": "4. state any five functions of money?",
        "keywords": {
            "store of value": 3,
            "unit of value": 2,
            "deffered payment": 3,
            "medium of exchange": 3,
            "unit of account": 1
        }
    },
    {
        "question": "5. Explain the process of photosynthesis.",
        "keywords": {
            "photosynthesis" : 2,
            "light energy": 1,
            "chemical energy" : 1,
            "chloroplasts" : 2,
            "chlorophyll" : 1,
            "carbon dioxide" : 1,
            "water" : 1,
            "glucose" : 1,
            "oxygen" :1,
            "atp" :1
            
        }
    }
]

total_score = 0
max_total_score = 0

print("Welcome to the ECN 101 (Theory Test)\n")

print("Kindly attempt the following questions.\n")

for q in questions:
    print(q["question"])
    answer = input("Enter Your answer: ").lower().strip()
    question_score = 0

    for keyword, weight in q["keywords"].items():
        max_total_score += weight
        if keyword in answer:
            question_score += weight
    total_score += question_score
    print(f"Points earned for this question: {question_score}\n")


print("Exam Completed!")
print(f"Your total score is: {total_score} out of {max_total_score}")


