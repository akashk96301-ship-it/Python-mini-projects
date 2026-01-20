def show_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)


def get_user_answer():
    while True:
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid choice. Please enter A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def update_score(is_correct, score):
    if is_correct:
        score += 1
    return score


def get_performance(score, total_questions):
    if score <= 1:
        return "Beginner"
    elif score <= 3:
        return "Intermediate"
    else:
        return "Expert"


def quiz_game(questions):
    score = 0

    for question in questions:
        show_question(question)
        user_answer = get_user_answer()
        is_correct = check_answer(user_answer, question["answer"])

        if is_correct:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Correct answer is {question['answer']}")

        score = update_score(is_correct, score)

    performance = get_performance(score, len(questions))

    print("\n🎯 QUIZ COMPLETED")
    print("Total Questions:", len(questions))
    print("Your Score:", score)
    print("Performance Level:", performance)


# ------------------ DATA ------------------

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. lambda"],
        "answer": "B"
    },
    {
        "question": "What does len([1,2,3]) return?",
        "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
        "answer": "B"
    }
]

# ------------------ START GAME ------------------

quiz_game(questions)
