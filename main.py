import tkinter as tk
from tkinter import simpledialog, messagebox
from models.question_loader import QuestionLoader
from models.quiz_engine import QuizEngine
from models.ui import QuizUI
from models.leaderboard import Leaderboard

def main():
    questions = QuestionLoader.load_from_csv("data/questions.csv")

    root = tk.Tk()
    root.withdraw()
    username = simpledialog.askstring("Welcome", "Enter your name:")
    root.deiconify()

    if not username:
        username = "Anonymous"

    if messagebox.askyesno("Leaderboard", "Want to see the leaderboard?"):
        Leaderboard.show_leaderboard()

    engine = QuizEngine(questions)
    app = QuizUI(root, engine, username)
    root.mainloop()

if __name__ == "__main__":
    main()
