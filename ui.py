from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self):
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
            text="The quiz question.",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
