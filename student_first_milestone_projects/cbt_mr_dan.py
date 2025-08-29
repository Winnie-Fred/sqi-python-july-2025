question_one = """Que: What is the color of the sky?
a) Pink
b) Blue
c) White
d) Orange
"""

question_two = """Que: What is the name of the strogest car?
a) Tesla
b) Bugatti
c) Ferrari
d) Benz
"""

question_three = """Que: What is the name of the fastest car?
a) Tesla
b) Bugatti
c) Ferrari
d) Benz
"""

question_four = """Que: What is the name of the fastest car?
a) Tesla
b) Bugatti
c) Ferrari
d) Benz
"""

question_five = """Que: What is the name of the fastest car?
a) Tesla
b) Bugatti
c) Ferrari
d) Benz
"""

cbt = [
    {
        "question": question_one,
        "ans": "d"
    },
    {
        "question": question_two,
        "ans": "d"
    },
    {
        "question": question_three,
        "ans": "d"
    },
    {
        "question": question_four,
        "ans": "d"
    },
    {
        "question": question_five,
        "ans": "d"
    },
]

print("Welcome to CBT Test")
header = """
#########################
#      TEST SCHOOL      #   
#########################
"""
print(header)

idx = 0
score = 0
while idx < len(cbt):
    print(idx+1, cbt[idx]["question"])
    user_ans = input("Choose an option between a - d: ").strip().lower()
    if user_ans not in ["a", "b", "c", "d"]:
        print("Invalid option. Pick again")
        continue
    if user_ans == cbt[idx]["ans"]:
        score +=1
    idx+=1
print(f"You score {score} out of {len(cbt)}")
