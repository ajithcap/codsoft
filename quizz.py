import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x600")  # Increased height to accommodate answer feedback

        # Define colors
        self.background_color = "#faf3b2"
        self.question_color = "#242423"
        self.option_color = "#bbd0ff"
        self.correct_color = "#6ba368"
        self.wrong_color = "#e01e37"

        # Create a frame to cover the entire window and set its background color
        self.frame = tk.Frame(root, bg=self.background_color)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Display rules and regulations
        self.title_heading=tk.Label(self.frame,text="QUIZZ",font=("Helvetica ",30),bg=self.question_color,fg="#f8961e")
        self.title_heading.pack(pady=25,fill=tk.X)

        
        
        self.rules_label = tk.Label(self.frame, text="Rules and Regulations:\n\n1. Answer all the questions.\n2. You have 10 seconds for each question.\n3. Click on an option to select your answer.", font=("Arial", 10), bg=self.background_color, fg="#4d194d")
        self.rules_label.pack(pady=20)

        # Create a question label
        self.question_label = tk.Label(self.frame, text="", font=("Arial", 12), bg=self.background_color, fg=self.question_color)
        self.question_label.pack(pady=10)

        # Create option buttons
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.frame, text="", font=("Arial", 10), bg=self.option_color, fg="white", width=20, height=2, command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)

        # Create labels for answer feedback
        self.feedback_label = tk.Label(self.frame, text="", font=("Arial", 10), bg=self.background_color, fg=self.correct_color)
        self.feedback_label.pack(pady=10)

        # Initialize quiz
        self.current_question = -1
        self.score = 0
        self.questions = [
            {
                'question': 'What is the largest mammal in the world?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Lion'],
                'correct': 'Blue Whale'
            },
            {
                'question': 'Which gas is most abundant in the Earth\'s atmosphere?',
                'options': ['Nitrogen', 'Oxygen', 'Carbon Dioxide', 'Hydrogen'],
                'correct': 'Nitrogen'
            },
            {
                'question': 'Which artist painted the Mona Lisa?',
                'options': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
                'correct': 'Leonardo da Vinci'
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'correct': 'Au'
            },
            {
                'question': 'Which planet is known as the "Morning Star" or "Evening Star"?',
                'options': ['Mars', 'Venus', 'Mercury', 'Saturn'],
                'correct': 'Venus'
            },
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Lungs', 'Skin'],
                'correct': 'Skin'
            },
            {
                'question': 'Who wrote the play "Romeo and Juliet"?',
                'options': ['William Shakespeare', 'Mark Twain', 'Charles Dickens', 'J.K. Rowling'],
                'correct': 'William Shakespeare'
            },
            {
                'question': 'What is the smallest prime number?',
                'options': ['1', '2', '3', '5'],
                'correct': '2'
            },
            {
                'question': 'Which mountain is the tallest in the world?',
                'options': ['Mount Kilimanjaro', 'Mount Everest', 'Mount McKinley', 'Mount Fuji'],
                'correct': 'Mount Everest'
            },
            {
                'question': 'What is the chemical symbol for water?',
                'options': ['H2O', 'CO2', 'O2', 'NaCl'],
                "correct": "H2O"
            },
            # Add more questions here
        ]
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            question_info = self.questions[self.current_question]
            self.question_label.config(text=question_info["question"])
            random.shuffle(question_info["options"])
            for i in range(4):
                self.option_buttons[i].config(text=question_info["options"][i], bg=self.option_color, fg="blue",font=(18))
            # Clear previous feedback
            self.feedback_label.config(text="")
        else:
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
            self.root.quit()

    def check_answer(self, choice):
        question_info = self.questions[self.current_question]
        if question_info["options"][choice] == question_info["correct"]:
            self.option_buttons[choice].config(bg=self.correct_color)
            self.feedback_label.config(text="Correct!", fg=self.correct_color)
            self.score += 1
        else:
            self.option_buttons[choice].config(bg=self.wrong_color)
            correct_option_index = question_info["options"].index(question_info["correct"])
            self.option_buttons[correct_option_index].config(bg=self.correct_color)
            self.feedback_label.config(text="Wrong! Correct answer: " + question_info["correct"], fg=self.wrong_color)
        self.root.after(1000, self.next_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
