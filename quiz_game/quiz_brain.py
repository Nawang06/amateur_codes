class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.length = len(q_list)
        self.score = 0
        self.question_number = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Category: {current_question.category}.")
        print(f"Difficulty: {current_question.difficulty}")
        user_answer = input(f"Q. {self.question_number}: {current_question.question}. ?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number == self.length:
            return False
        return True

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You Got It Right!!")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {c_answer}.")
        print(f"Your Score: {self.score}/{self.question_number}\n")
