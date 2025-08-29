import random

cbt_questions: list[dict[str, str | dict[str, str | int]]] = [
    {
        "question": "What is 2 + 2?",
        "options": {"a": 3, "b": 4,  "c": 5, "d": 6},
        "answer": "b",
        "score": 4
    },

    {
        "question": "What color is the sky on a clear day?",
        "options": {"a": "Red", "b": "Blue",  "c": "Green", "d": "Yellow"},
        "answer": "b",
        "score": 2
   },
   { 
        "question": "How many legs does a spider have?",
        "options": {"a": 6, "b": 7,  "c": 8, "d": 9},
        "answer": "c",
        "score": 1
   },
   {
        "question": "What sound does a cow make?",
        "options": {"a": "Meow", "b": "Bark",  "c": "Moo", "d": "Quack"},
        "answer": "c",
        "score": 6
    },
    {
        "question":"What is the opposite of 'hot'?",
        "options": {"a": "Warm", "b": "Cold",  "c": "Cool", "d": "Boiling"},
        "answer": "b",
        "score": 3
    }
]

random.shuffle(cbt_questions)
final_score = 0
total = 0

username = input("enter your preferrred username: ").strip().capitalize()
instruction = f"Each question carries 1 mark.\n Attempt all {len(cbt_questions)} questions"
print()
print(f"Hello {username}, Welcome To SQI Computer - Based - Test.\n\n Kindly read the exam instruction.\n\n {instruction}.\n")



for idx, q in enumerate(cbt_questions, start=1):
    print(f"{idx}. {q["question"]}")
    for option_letter, option_value in q["options"].items():
        print(f"({option_letter}). {option_value}")
       
    choice = ""
    while True:
        choice = input("enter your answer from A-D: ").lower().strip() 
        if choice not in "abcd":
            print("invalid entry, kindly choose option from A-D")
            continue
        break

    total += q["score"]
    answer = q["answer"]
    if choice == answer:
        final_score += q["score"]
        print("Correct Answer")
    else:
        print(f"Incorrect answer! correct answer is {answer} = {q["options"][answer]}")
print("Quiz completed.\n")
print(f"At the end of the quiz, {username}'s final score is {final_score} out of {total} questions")
