from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random


question_bank = []
for x in range(0, len(question_data)):
    question_bank.append(Question(question_data[x]['question'], question_data[x]['correct_answer']))

quiz = QuizBrain(question_bank)

run = True
while run == True:
    quiz.next_question()
    run = quiz.still_has_questions()

print("You finished the quiz!")
print(f"Your final quiz score is: {quiz.score}/{len(question_bank)}")