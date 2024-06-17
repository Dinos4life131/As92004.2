import tkinter as tk
from tkinter import messagebox
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        
        self.infinite_rounds = False
        self.num_rounds = 0
        self.topic_choice = 0
        self.topic_name = ""
        self.correct_count = 0
        self.wrong_answers = []
        self.unanswered_questions = []
        self.invalid_questions_count = 0
        self.round_counter = 0
        self.all_answers = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.instructions = tk.Label(self.root, text="Welcome to the Math Quiz!\nPlease follow the instructions below.", font=("Helvetica", 14))
        self.instructions.pack(pady=10)

        self.rounds_label = tk.Label(self.root, text="Enter the number of rounds you want to play (leave blank for infinite):", font=("Helvetica", 12))
        self.rounds_label.pack(pady=5)
        self.rounds_entry = tk.Entry(self.root)
        self.rounds_entry.pack(pady=5)
        self.rounds_entry.bind("<Return>", self.start_quiz)  # Bind Enter key to submit the number of rounds

        self.topics_label = tk.Label(self.root, text="Choose a topic:", font=("Helvetica", 12))
        self.topics_label.pack(pady=5)
        
        self.topic_var = tk.IntVar()
        self.topic_var.set(1)  # Default to first topic
        self.topics = {
            1: "Multiplication",
            2: "Addition",
            3: "Subtraction"
        }
        
        for key, value in self.topics.items():
            rb = tk.Radiobutton(self.root, text=value, variable=self.topic_var, value=key, font=("Helvetica", 12))
            rb.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Helvetica", 12))
        self.start_button.pack(pady=10)
    
    def start_quiz(self, event=None):
        number_of_rounds = self.rounds_entry.get().strip()
        
        if number_of_rounds == "":
            self.infinite_rounds = True
            self.num_rounds = None
            messagebox.showinfo("Info", "Infinite rounds it is!\nIf you want to end the quiz, type 'end' during the quiz.")
        elif number_of_rounds.isdigit() and int(number_of_rounds) > 0:
            self.num_rounds = int(number_of_rounds)
            self.infinite_rounds = False
            messagebox.showinfo("Info", f"{self.num_rounds} rounds it is!")
        else:
            messagebox.showerror("Error", "Invalid input! Please enter a positive number or leave blank for infinite rounds.")
            return
        
        self.topic_choice = self.topic_var.get()
        self.topic_name = self.topics[self.topic_choice]
        
        self.instructions.pack_forget()
        self.rounds_label.pack_forget()
        self.rounds_entry.pack_forget()
        self.topics_label.pack_forget()
        self.start_button.pack_forget()
        
        for widget in self.root.pack_slaves():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()
        
        self.ask_question()

    def ask_question(self):
        if not self.infinite_rounds and self.round_counter >= self.num_rounds:
            self.end_quiz()
            return

        self.questions = self.generate_questions(self.topic_choice, 1)
        self.question, self.answer = self.questions[0]
        
        self.question_frame = tk.Frame(self.root)
        self.question_frame.pack(pady=10)
        
        self.question_label = tk.Label(self.question_frame, text=f"Question {self.round_counter + 1}: {self.question}", font=("Helvetica", 14))
        self.question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(self.question_frame)
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)  # Bind Enter key to submit the answer
        
        self.submit_button = tk.Button(self.question_frame, text="Submit Answer", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=10)
    
    def check_answer(self, event=None):
        self.answer_entry.config(state=tk.DISABLED)  # Disable the entry field
        self.submit_button.config(state=tk.DISABLED)  # Disable the submit button

        user_input = self.answer_entry.get().strip().lower()
        if user_input == "end":
            self.infinite_rounds = False
            self.end_quiz()
            return
        
        result_text = ""
        try:
            user_answer = int(user_input) if user_input.isdigit() else user_input
            
            if user_answer == self.answer:
                self.correct_count += 1
                result_text = "Correct!"
            else:
                self.wrong_answers.append((self.question, user_answer, self.answer))
                result_text = f"Wrong! The correct answer is {self.answer}."
        
        except ValueError:
            self.invalid_questions_count += 1
            result_text = "Invalid input! Please enter a number."
        
        self.round_counter += 1
        self.question_label.config(text=f"Question {self.round_counter}: {self.question}\n{result_text}")
        
        self.answer_entry.delete(0, tk.END)
        self.root.after(2000, self.next_question)  # Wait 2 seconds before moving to the next question
    
    def next_question(self):
        self.question_frame.pack_forget()
        self.ask_question()

    def generate_questions(self, topic, num_questions):
        questions = []
        for _ in range(num_questions):
            if topic == 1:
                num3 = random.randint(1, 10)
                num4 = random.randint(1, 10)
                question = f"What is {num3} * {num4}?"
                answer = num3 * num4
            elif topic == 2:
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)
                question = f"What is {num1} + {num2}?"
                answer = num1 + num2
            elif topic == 3:
                num1 = random.randint(0, 100)
                num2 = random.randint(0, 100)
                if num1 < num2:
                    num1, num2 = num2, num1
                question = f"What is {num1} - {num2}?"
                answer = num1 - num2
            questions.append((question, answer))
        return questions

    def end_quiz(self):
        for widget in self.root.pack_slaves():
            widget.pack_forget()
        
        total_valid_questions = self.correct_count + len(self.wrong_answers) - self.invalid_questions_count
        result_message = f"You answered {self.correct_count} out of {total_valid_questions} valid questions correctly.\n"
        if total_valid_questions > 0:
            percentage_correct = (self.correct_count / total_valid_questions) * 100
            rounded_percentage = round(percentage_correct)
            result_message += f"You got {rounded_percentage}% correct!"
        
        messagebox.showinfo("Quiz Over", result_message)
        
        if self.wrong_answers:
            review_message = "You have some wrong answers. Do you want to review them?"
            if messagebox.askyesno("Review", review_message):
                self.review_wrong_answers()
        
        if messagebox.askyesno("Play Again", "Do you want to play again?"):
            self.reset_quiz()
        else:
            self.root.quit()

    def review_wrong_answers(self):
        review_window = tk.Toplevel(self.root)
        review_window.title("Review Wrong Answers")
        
        review_text = tk.Text(review_window, wrap=tk.WORD, width=50, height=20, font=("Helvetica", 12))
        review_text.pack(pady=10)
        
        for i, (question, user_answer, correct_answer) in enumerate(self.wrong_answers):
            review_text.insert(tk.END, f"{i + 1}. {question}\nYour answer: {user_answer}\nCorrect answer: {correct_answer}\n\n")
        
        review_text.config(state=tk.DISABLED)
    
    def reset_quiz(self):
        self.infinite_rounds = False
        self.num_rounds = 0
        self.topic_choice = 0
        self.topic_name = ""
        self.correct_count = 0
        self.wrong_answers = []
        self.unanswered_questions = []
        self.invalid_questions_count = 0
        self.round_counter = 0
        self.all_answers = []
        
        for widget in self.root.pack_slaves():
            widget.pack_forget()
        
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

