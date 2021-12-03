from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(bg=THEME_COLOR, fg="white", text="Score: 0")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(
            background="white",
            width=300,
            height=250,
            highlightthickness=0,
        )
        self.quiz_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="The quiz question.",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_question, text=question)

    def answer_true(self):
        right_or_wrong = self.quiz.check_answer("True")
        self.user_feedback(right_or_wrong)

    def answer_false(self):
        right_or_wrong = self.quiz.check_answer("False")
        self.user_feedback(right_or_wrong)

    def user_feedback(self, right_or_wrong: bool):
        if right_or_wrong == True:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
