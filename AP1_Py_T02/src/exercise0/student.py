
class Student:
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
        self.status = 'Очередь'
        self.exam_time = float('inf')

    def get_name(self) -> str:
        return self.name

    def get_gender(self) -> str:
        return self.gender

    def get_status(self):
        return self.status

    def get_exam_time(self):
        return self.exam_time
