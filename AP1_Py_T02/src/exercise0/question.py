class Question:
    def __init__(self, question: str):
        self.question = question
        self.count_of_correct_answers = 0

    def get_words(self):
        return self.question.split()
