import html

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        return f'Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False): ' #use html entities unescaped


    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False