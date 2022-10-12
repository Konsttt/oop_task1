from utils import logger


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Средняя оценка вычисляется как сквозная - по всем оценкам за все курсы.
    def __average_rating(self):
        sum_, count_ = 0, 0
        if len(self.grades) > 0:
            for value_list in self.grades.values():
                sum_ += sum(value_list)
                count_ += len(value_list)
            s = round(sum_ / count_, 2)
        else:
            s = 'у данного студента пока нет оценок.'
        return s

    def __str__(self):
        if len(self.courses_in_progress) > 0:
            courses = ', '.join(self.courses_in_progress)
        else:
            courses = 'у данного студента сейчас нет активных курсов.'
        if len(self.finished_courses) > 0:
            courses_f = ', '.join(self.finished_courses)
        else:
            courses_f = 'у данного студента нет завершенных курсов.'
        s = '\n'.join([f'Имя: {self.name}',
                       f'Фамилия: {self.surname}',
                       f'Средняя оценка за домашние задания: {self.__average_rating()}',
                       f'Курсы в процессе изучения: {courses}',
                       f'Завершенные курсы: {courses_f}'])
        return s

    def __lt__(self, other):
        s = self.__pre_compare(other)
        if type(s) != str:
            return s[0] < s[1]
        else:
            return s

    def __eq__(self, other):
        s = self.__pre_compare(other)
        if type(s) != str:
            return s[0] == s[1]
        else:
            return s

    #  Проверка перед сравнением. На случай, если у студентов нет ни одной оценки - возвращает сообщение(строку).
    #  А также, чтобы не было больших кусков одинакового кода в __lt__ и __eq__
    def __pre_compare(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        else:
            x_student = self.__average_rating()
            y_student = other.__average_rating()
            if type(x_student) == str:
                return f'У студента {self.name} {self.surname} пока нет оценок.'
            elif type(y_student) == str:
                return f'У студента {other.name} {other.surname} пока нет оценок.'
            elif type(x_student) == str and type(y_student) == str:
                return f'У данных студентов пока нет оценок.'
            else:
                return [x_student, y_student]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        s = '\n'.join([f'Имя: {self.name}',
                       f'Фамилия: {self.surname}',
                       f'Средняя оценка за лекции: {self.__average_rating()}'])
        return s

    #  Средняя оценка вычисляется как сквозная по всем лекциям для всех курсов
    def __average_rating(self):
        sum_, count_ = 0, 0
        if len(self.grades) > 0:
            for value_list in self.grades.values():
                sum_ += sum(value_list)
                count_ += len(value_list)
            s = round(sum_ / count_, 2)
        else:
            s = 'у данного лектора пока нет оценок.'
        return s

    def __lt__(self, other):
        s = self.__pre_compare(other)
        if type(s) != str:
            return s[0] < s[1]
        else:
            return s

    def __eq__(self, other):
        s = self.__pre_compare(other)
        if type(s) != str:
            return s[0] == s[1]
        else:
            return s

    #  Проверка перед сравнением. На случай, если у лекторов нет ни одной оценки - возвращает сообщение(строку).
    #  А также, чтобы не было больших кусков одинакового кода в __lt__ и __eq__
    def __pre_compare(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer'
        else:
            x_lector = self.__average_rating()
            y_lector = other.__average_rating()
            if type(x_lector) == str:
                return f'У лектора {self.name} {self.surname} пока нет оценок.'
            elif type(y_lector) == str:
                return f'У лектора {other.name} {other.surname} пока нет оценок.'
            elif type(x_lector) == str and type(y_lector) == str:
                return f'У данных лекторов пока нет оценок.'
            else:
                return [x_lector, y_lector]


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        s = '\n'.join([f'Имя: {self.name}', f'Фамилия: {self.surname}'])
        return s


#  Средняя оценка по курсу у списка студентов
@logger(path_filename='C:/Users/konst/PycharmProjects/oop_task1/logfile.txt')
def average_st_list(course_name, st_list):
    sum_ = 0
    count_ = 0
    average_rate = 0
    for st in st_list:
        if not isinstance(st, Student):
            print('Not a Student')
            return 'Not a Student'
        else:
            sum_ += sum(st.grades[course_name])
            count_ += len(st.grades[course_name])
            average_rate = round(sum_ / count_, 2)
    print(average_rate)
    return average_rate


#  Средняя оценка по лекциям курса у списка лекторов
@logger(path_filename='C:/Users/konst/PycharmProjects/oop_task1/logfile.txt')
def average_lc_list(course_name, lc_list):
    sum_ = 0
    count_ = 0
    average_rate = 0
    for lc in lc_list:
        if not isinstance(lc, Lecturer):
            print('Not a Lecturer')
            return 'Not a Lecturer'
        else:
            sum_ += sum(lc.grades[course_name])
            count_ += len(lc.grades[course_name])
            average_rate = round(sum_ / count_, 2)
    print(average_rate)
    return average_rate


best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python backend']

student2 = Student('Name2', 'Surname2', 'man')
student2.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(student2, 'Python', 7)
cool_reviewer.rate_hw(student2, 'Python', 8)
cool_reviewer.rate_hw(student2, 'Python', 9)

lecturer1 = Lecturer('Guido', 'van Rossum')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Python backend']

lecturer2 = Lecturer('Super', 'Lector')
lecturer2.courses_attached += ['Python']

best_student.rate_lecturer(lecturer1, 'Python', 10)
best_student.rate_lecturer(lecturer1, 'Python', 11)
best_student.rate_lecturer(lecturer1, 'Python backend', 11)

best_student.rate_lecturer(lecturer2, 'Python', 9)
best_student.rate_lecturer(lecturer2, 'Python', 10)


print(cool_reviewer)
print()
print(lecturer1)
print()
print(best_student)
print()
print(best_student > student2)
print()
print(lecturer1 == lecturer2)
print()
average_st_list('Python', [best_student, student2])
print()
average_lc_list('Python', [lecturer1, lecturer2])
