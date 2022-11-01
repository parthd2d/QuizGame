from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n\nYou've finished the quiz!!!")
print(f"Your final score is: {quiz.score}/{len(quiz.questions_list)}")

