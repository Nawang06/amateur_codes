from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_info = Question(question["question"], question["correct_answer"], question["difficulty"], question["category"])
    question_bank.append(question_info)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("YOU'VE COMPLETED THE QUIZ!")
print(f"Your Final Score Is: {quiz.score}/{quiz.length}")