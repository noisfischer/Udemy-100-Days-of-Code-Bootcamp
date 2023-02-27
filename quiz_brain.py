class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}.: {current_question.question_text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('\nYou answered correctly!\n')
            self.score += 1
        else:
            print('\nYou answered wrong.\n')
        print(f'The correct answer was: {correct_answer}')
        print(f"Your current score is {self.score}/{self.question_number}\n")