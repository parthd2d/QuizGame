def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ").lower()
        if check_answer(user_answer, (curr_question.answer).lower()):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {curr_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")


    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
