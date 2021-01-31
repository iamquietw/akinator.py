questions = [
    "Это человек?",
    "Это живое?",
    "Это жидкость?"
    ]

data = {
    "0": {
        "object": "Чай",
        "answers": [0, 0, 1]
    },
    "1": {
        "object": "Какой-то человек",
        "answers": [1, 1, 0]
    },
    "2": {
        "object": "Кто-то живой, но не человек",
        "answers": [0, 1, 0]
    }
}

while True:
    answers = []
    current_question = 0
    while len(answers) != len(questions):
        answer = input(questions[current_question] + " >> ")
        current_question = current_question + 1
        answers.append(int(answer))
    answer = ""
    for item in data:
        matches = 0
        for i in range(len(questions)):
            if answers[i] == data[item]["answers"][i]:
                matches = matches + 1
        if matches == len(questions):
            answer = data[item]["object"]
    print(answer)
