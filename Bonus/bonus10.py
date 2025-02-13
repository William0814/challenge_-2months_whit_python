import json


with open('question.json', 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for q in data:
    print(q["question_text"])
    for index, alternative in enumerate(q["alternatives"]):
        print(index + 1, "-", alternative)
    user_select = int(input("Enter your answer: "))
    q["user_select"] = user_select
    if q["user_select"] == q["correct_answer"]:
        score = score + 1


for index, question in enumerate(data):
    if question["user_select"] == question["correct_answer"]:
        score = score + 1
        result = 'Correct answer'
    else:
        result = 'Wrong answer'

    message = f"{index + 1} {result} - Your answer: {question['user_select']}, "\
              f"Correct answer: {question['correct_answer' ]}"
    print(message)


print(score, "/", len(data))