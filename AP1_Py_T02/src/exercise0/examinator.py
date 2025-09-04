import random

class Examinator:
    def __init__(self, name: str, gender: str):
        self.mood = None
        self.name = name
        self.gender = gender
        self.current_student = '-'
        self.count_of_students = 0
        self.count_of_failed_students = 0
        self.work_time = 0

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def exam_duration(self) -> float:
        work_time = random.uniform(len(self.name) - 1, len(self.name) + 1)
        return work_time

    def get_answers_list(self, answer_question, question) -> list[str]:
        result = []
        words = [i for i in question.get_words()]
        word = answer_question(self, words)
        words.remove(word)
        result.append(word)
        while random.choices([True, False], weights=[1 / 3, 2 / 3], k=1)[0] and len(words) > 0:
            word = answer_question(self, words)
            words.remove(word)
            result.append(word)

        return result

    def get_mood(self):
        self.mood = random.choices(['bad', 'good', 'neutral'], weights=[1 / 8, 1 / 4, 5 / 8], k=1)[0]
        return self.mood
