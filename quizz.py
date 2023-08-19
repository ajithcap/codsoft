import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Knowledge Quiz")
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Paris', 'London', 'Berlin', 'Rome'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'What is the largest mammal in the world?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Lion'],
                'correct_answer': 'Blue Whale'
            },
            {
                'question': 'Which gas is most abundant in the Earth\'s atmosphere?',
                'options': ['Nitrogen', 'Oxygen', 'Carbon Dioxide', 'Hydrogen'],
                'correct_answer': 'Nitrogen'
            },
            {
                'question': 'Which artist painted the Mona Lisa?',
                'options': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
                'correct_answer': 'Leonardo da Vinci'
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'correct_answer': 'Au'
            },
            {
                'question': 'Which planet is known as the "Morning Star" or "Evening Star"?',
                'options': ['Mars', 'Venus', 'Mercury', 'Saturn'],
                'correct_answer': 'Venus'
            },
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Lungs', 'Skin'],
                'correct_answer': 'Skin'
            },
            {
                'question': 'Who wrote the play "Romeo and Juliet"?',
                'options': ['William Shakespeare', 'Mark Twain', 'Charles Dickens', 'J.K. Rowling'],
                'correct_answer': 'William Shakespeare'
            },
            {
                'question': 'What is the smallest prime number?',
                'options': ['1', '2', '3', '5'],
                'correct_answer': '2'
            },
            {
                'question': 'Which mountain is the tallest in the world?',
                'options': ['Mount Kilimanjaro', 'Mount Everest', 'Mount McKinley', 'Mount Fuji'],
                'correct_answer': 'Mount Everest'
            },
            {
                'question': 'What is the chemical symbol for water?',
                'options': ['H2O', 'CO2', 'O2', 'NaCl'],
                'correct_answer': 'H2O'
            }
        ]
        
        random.shuffle(self.questions)
        self.random_questions = self.questions[:10]

        self.label = tk.Label(root, text="Welcome to the General Knowledge Quiz!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", command=partial(self.check_answer, _))
            self.option_buttons.append(button)
            button.pack(fill=tk.BOTH, padx=20, pady=5)

        self.correct_answer_label = tk.Label(root, text="", fg="green")
        self.correct_answer_label.pack()

        self.next_question_button = tk.Button(root, text="Next Question", command=lambda: self.next_question())
        self.next_question_button.pack(pady=10)
        self.next_question_button.config(state=tk.DISABLED)

        self.load_question(0)

    def load_question(self, question_index):
        self.current_question = question_index
        question_data = self.random_questions[question_index]
        self.question_label.config(text=question_data['question'])
        options = question_data['options']
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)
        self.next_question_button.config(state=tk.DISABLED)

    def check_answer(self, selected_option):
        correct_answer = self.random_questions[self.current_question]['correct_answer']
        if self.random_questions[self.current_question]['options'][selected_option] == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.correct_answer_label.config(text="Your answer is correct.", fg="green")
        else:
            correct_option = self.random_questions[self.current_question]['options'].index(correct_answer)
            self.correct_answer_label.config(text=f"Your answer is incorrect. Correct answer: {correct_answer}", fg="red")
        self.next_question_button.config(state=tk.NORMAL)

    def next_question(self):
        if self.current_question < len(self.random_questions) - 1:
            self.load_question(self.current_question + 1)
        else:
            self.correct_answer_label.config(text="")
            messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
