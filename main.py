from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

quiz_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain)

quiz_ui.canvas.itemconfig(quiz_ui, text=quiz.next_question())

print(f'You\'ve completed the quiz '
      f'\nYour final score was {quiz.score}/{quiz.question_number}')