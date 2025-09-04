import copy
import os
import random
import time
import multiprocessing as mp
from multiprocessing.managers import NamespaceProxy, BaseManager
from examinator import Examinator
from question import Question
from student import Student
from prettytable import PrettyTable


def get_exam_questions(self, questions: list['Question']) -> list['Question']:
    return random.sample(questions, k=3)


def load_students(filename: str, manager) -> list['Student']:
    return list(
        map(lambda line: manager.StudentRegistred(line[0], 'male' if line[1] == 'М' else 'female'),
            (line.split() for line in open(filename))))


def load_examinators(filename: str, manager) -> list['Examinator']:
    return list(
        map(lambda line: manager.ExaminatorRegistred(line[0], 'male' if line[1] == 'М' else 'female'),
            (line.split() for line in open(filename))))


def load_questions(filename: str, manager) -> list['Question']:
    return list(map(lambda line: manager.QuestionRegistred(line), open(filename)))


def answer_question(human, words) -> str:
    n = len(words) * (len(words) + 1) / 2
    if human.get_gender() == 'male':
        weights = [(len(words) - i) / n for i in range(len(words))]
    else:
        weights = [(i + 1) / n for i in range(len(words))]
    return random.choices(words, weights=weights, k=1)[0]


def conduct_exam(examinator, student, exam_questions, examinators, students, start_time):
    exam_duration = examinator.exam_duration()
    examinator.current_student = student.name
    examinator.count_of_students += 1
    print_status(examinators, students, start_time)
    time.sleep(exam_duration)
    examinator.work_time += exam_duration
    student.exam_time = exam_duration
    examinator_mood = examinator.get_mood()
    correct_answer = 0
    wrong_answer = 0

    for question in exam_questions:
        if answer_question(student, question.get_words()) in examinator.get_answers_list(answer_question, question):
            correct_answer += 1
            question.count_of_correct_answers += 1
        else:
            wrong_answer += 1

    if examinator_mood == 'bad':
        examinator.count_of_failed_students += 1
        student.status = 'Провалил'
    elif examinator_mood == 'good':
        student.status = 'Сдал'
    else:
        if wrong_answer > correct_answer:
            student.status = 'Провалил'
            examinator.count_of_failed_students += 1
        else:
            student.status = 'Сдал'
    if (time.time() - start_time) > 30:
        time.sleep(random.uniform(12, 18))
    examinator.current_student = '-'
    print_status(examinators, students, start_time)


def check_changes_students(old, new):
    for i in range(len(old)):
        if old[i].status != new[i].status:
            return True
    return False


def check_changes_examinators(old, new):
    for i in range(len(old)):
        if old[i].current_student != new[i].current_student or old[i].count_of_students != new[i].count_of_students:
            return True
    return False


def create_print_form(examinators, students):
    os.system('clear')
    students_table = PrettyTable()
    examinators_table = PrettyTable()
    students_table.field_names = ['Студент', 'Статус']
    students_table.align['Студент'] = 'l'
    students_table.align['Статус'] = 'c'
    sorted_students = sorted(students, key=lambda student: (
        student.get_status() != 'Очередь', student.get_status() != 'Сдал', student.get_status()))
    students_table.add_rows([student.get_name(), student.get_status()] for student in sorted_students)

    examinators_table.field_names = ['Экзаменатор', 'Текущий студент', 'Всего студентов', 'Завалил', 'Время работы']
    examinators_table.add_rows([examinator.get_name(), examinator.current_student, examinator.count_of_students,
                                examinator.count_of_failed_students, ' %.2f' % examinator.work_time] for examinator in
                               examinators)
    return students_table, examinators_table


def print_status(examinators, students, start_time):
    os.system('clear')
    students_table, examinators_table = create_print_form(examinators, students)
    print(students_table, '\n')
    print(examinators_table)
    print("Осталось в очереди: ", [student.get_status() for student in students].count('Очередь'), " из ",
          len(students))
    print("Время с момента начала экзамена: %.2f" % (time.time() - start_time))


def print_final_status(examinators, students, questions, start_time):
    students_table, examinators_table = create_print_form(examinators, students)
    print(students_table, '\n')
    print(examinators_table)
    print("Время с момента начала экзамена и до момента и его завершения: %.2f" % (time.time() - start_time))
    best_student_min_time = min(student.get_exam_time() for student in students if student.status == 'Сдал')
    print("Имена лучших студентов:",
          ", ".join(student.get_name() for student in students if
                    student.get_exam_time() == best_student_min_time and student.status == 'Сдал'))
    examinator_min_time = min(
        examinator.count_of_failed_students / examinator.count_of_students for examinator in examinators)
    print("Имена лучших экзаменаторов:", ", ".join(examinator.get_name() for examinator in examinators if
                                                   examinator.count_of_failed_students / examinator.count_of_students == examinator_min_time))
    bad_student_min_time = min(student.get_exam_time() for student in students if student.status == 'Провалил')
    print("Имена студентов, которых после экзамена отчислят:",
          ", ".join(student.get_name() for student in students if
                    student.get_exam_time() == bad_student_min_time and student.status == 'Провалил'))
    best_question_time = max(question.count_of_correct_answers for question in questions)
    print("Лучшие вопросы:", ", ".join(
        question.question.strip() for question in questions if question.count_of_correct_answers == best_question_time))
    count_of_good_students = len([student for student in students if student.status == 'Сдал'])
    print('Вывод:', 'экзамен не удался' if count_of_good_students / len(students) <= 0.85 else 'экзамен удался')


BaseManager.register('StudentRegistred', Student, NamespaceProxy)
BaseManager.register('ExaminatorRegistred', Examinator, NamespaceProxy)
BaseManager.register('QuestionRegistred', Question, NamespaceProxy)


def main():
    start_time = time.time()
    M = BaseManager()
    M.start()
    students = load_students("students.txt", M)
    questions = load_questions("questions.txt", M)
    examinators = load_examinators("examiners.txt", M)

    examinators_old = copy.deepcopy(examinators)
    students_old = copy.deepcopy(students)
    print_status(examinators, students, start_time)
    processes = []
    num = 0
    while num < len(students):
        exam_questions = random.sample(questions, k=3)
        free_examinators = [i for i in examinators if i.current_student == '-']
        if len(free_examinators) > 0:
            examinator = random.sample(free_examinators, k=1)[0]
            num += 1
            process = mp.Process(target=conduct_exam, args=(
                examinator, students[num - 1], exam_questions, examinators, students, start_time,))
            processes.append(process)
            process.start()

        if check_changes_examinators(examinators_old, examinators) or check_changes_students(students_old, students):
            print_status(examinators, students, start_time)
        time.sleep(0.01)
        examinators_old = copy.deepcopy(examinators)
        students_old = copy.deepcopy(students)

    for process in processes:
        process.join()

    print_final_status(examinators, students, questions, start_time)


if __name__ == '__main__':
    main()
