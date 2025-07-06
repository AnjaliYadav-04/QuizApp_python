import csv
import random
from models.question import Question

class QuestionLoader:
    @staticmethod
    def load_from_csv(filepath):
        questions = []
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                prompt = row["prompt"]
                options = [row["option1"], row["option2"], row["option3"], row["option4"]]
                answer = row["answer"]
                questions.append(Question(prompt, options, answer))
        random.shuffle(questions)
        return questions
