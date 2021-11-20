from Question import Question

question_prompts = [
    "What is my favorite color?\na) pink\nb) blue\nc) purple\nd) all of them\n",
    "What is the color of sky?\na) pink\nb) blue\nc) purple\nd) all of them\n"
]

question_answers = [
    'd',
    'b'
]

questions = [
    Question(question_prompts[i], question_answers[i]) for i in range(len(question_prompts))
]


def run_test(questions=questions):
    score = 0
    for question in questions:
        if input(question.prompt) == question.answer:
            score += 1

    print("------------------------------------")
    print("You got " + str(score) + "/" +
          str(len(question_prompts)) + " correct")


run_test()
