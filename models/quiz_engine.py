class QuizEngine:
    def __init__(self, questions):
        self.questions = questions
        self.index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.index]

    def check_answer(self, selected):
        if selected == self.questions[self.index].answer:
            self.score += 1
            return True
        return False

    def has_next(self):
        return self.index < len(self.questions) - 1

    def next_question(self):
        self.index += 1

    def get_score(self):
        return self.score

    def total_questions(self):
        return len(self.questions)
