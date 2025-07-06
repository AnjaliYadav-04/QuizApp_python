import tkinter as tk
from tkinter import messagebox

class QuizUI:
    def __init__(self, root, engine, username, timer_seconds=10):
        self.root = root
        self.engine = engine
        self.username = username
        self.timer_seconds = timer_seconds
        self.time_left = timer_seconds
        self.timer_id = None

        self.var = tk.StringVar()
        self.root.title("Quiz App")
        self.root.geometry("400x320")

        self.timer_label = tk.Label(root, text="Time Left:", font=("Arial", 12))
        self.timer_label.pack(pady=5)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12), anchor='w', justify='left')
            rb.pack(fill='x', padx=20)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_clicked)
        self.next_button.pack(pady=20)

        self.display_question()

    def start_timer(self):
        self.time_left = self.timer_seconds
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time Left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.next_clicked(auto=True)

    def display_question(self):
        q = self.engine.get_current_question()
        self.var.set(None)
        self.question_label.config(text=f"Q{self.engine.index + 1}: {q.prompt}")
        for i, option in enumerate(q.options):
            self.radio_buttons[i].config(text=option, value=option)
        self.start_timer()

    def next_clicked(self, auto=False):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        selected = self.var.get()
        if not selected and not auto:
            messagebox.showwarning("No selection", "Please select an option.")
            return

        self.engine.check_answer(selected)

        if self.engine.has_next():
            self.engine.next_question()
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        from models.result_saver import ResultSaver
        score = self.engine.get_score()
        total = self.engine.total_questions()
        ResultSaver.save_to_csv(self.username, score, total)
        messagebox.showinfo("Quiz Completed", f"{self.username}, your score: {score}/{total}")
        self.root.quit()
