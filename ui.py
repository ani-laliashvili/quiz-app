import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=500, width=300)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tkinter.Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "normal"))
        self.score.grid(row=0, column=1, pady=20, padx=20)


        self.canvas = tkinter.Canvas(height=250, width=300, bg="white")
        self.question_text = self.question_text = self.canvas.create_text(150, 125,
                                                                          text=" ",
                                                                          width=280,
                                                                          font=("Arial", 20, "italic"),
                                                                          fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true = tkinter.PhotoImage(file="images/true.png")
        false = tkinter.PhotoImage(file="images/false.png")

        self.false_btn = tkinter.Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)
        self.true_btn = tkinter.Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)