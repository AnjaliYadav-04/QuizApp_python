import csv
import tkinter as tk
from tkinter import ttk
import os

class Leaderboard:
    @staticmethod
    def show_leaderboard(filename="data/result.csv"):  # 
        win = tk.Toplevel()
        win.title("Leaderboard")
        win.geometry("400x300")

        # Set up the table
        tree = ttk.Treeview(win, columns=("Username", "Score", "Total"), show='headings')
        tree.heading("Username", text="Username")
        tree.heading("Score", text="Score")
        tree.heading("Total", text="Total")
        tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Check if file exists
        if not os.path.exists(filename):
            tree.insert("", "end", values=("No data yet", "-", "-"))
            return

        try:
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

                # If file has header but no data
                if not rows:
                    tree.insert("", "end", values=("No quiz attempts yet", "-", "-"))
                    return

                # Show last 10 results
                for row in reversed(rows[-10:]):
                    tree.insert("", "end", values=(row["Username"], row["Score"], row["Total"]))

        except Exception as e:
            tree.insert("", "end", values=(f"Error: {e}", "-", "-"))
