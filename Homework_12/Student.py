import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value.istitle():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы.")
        instance.__dict__[self.name] = value


class SubjectValidator:
    def __init__(self, allowed_subjects):
        self.allowed_subjects = allowed_subjects

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value not in self.allowed_subjects:
            raise ValueError(f"Предмет {value} не допускается.")
        instance.__dict__[self.name] = value


class CSV:

    def __init__(self, lessons_list):
        self.__create_csv(lessons_list)

    @property
    def get_lessons(self):
        with open('lessons.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            temp = []
            for row in reader:
                temp.append(row['Предметы'])
        return temp

    def __create_csv(self, lessons_list):
        with open('lessons.csv', 'w', newline='', encoding='utf-8') as new_file_csv:
            csv_write = csv.DictWriter(new_file_csv, fieldnames=["Предметы"])
            csv_write.writeheader()
            all_data = []
            for lesson in lessons_list:
                temp = {'Предметы': lesson}
                all_data.append(temp)
            csv_write.writerows(all_data)


class Student:
    name = NameValidator()
    lessons = CSV(["Математика", "Физика", "Химия"])
    subjects = SubjectValidator(lessons.get_lessons)

    def __init__(self, name):
        self.name = name
        self.grades = {}
        self.test_results = {}

    def add_grade(self, subject, grade):
        min_score = 2
        max_score = 5
        if grade in range(min_score, max_score + 1):
            if subject not in self.grades:
                self.subjects = subject
                self.grades[subject] = []
        else:
            raise ValueError(f"Оценка {grade} не допускается.")
        self.grades[subject].append(grade)

    def add_test_result(self, subject, result):
        min_score = 0
        max_score = 100
        if result in range(min_score, max_score + 1):
            if subject not in self.test_results:
                self.subjects = subject
                self.test_results[subject] = []
        else:
            raise ValueError(f"Оценка {result} не допускается.")
        self.test_results[subject].append(result)

    def get_subject_average_grade(self, subject):
        if subject not in self.grades:
            return 0
        return sum(self.grades[subject]) / len(self.grades[subject])

    def get_overall_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_subjects = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_subjects


if __name__ == '__main__':
    student = Student("Титов Артём Евгеньевич")
    print(student.name)

    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_grade("Физика", 3)

    student.add_test_result("Математика", 80)
    student.add_test_result("Математика", 90)
    student.add_test_result("Физика", 75)

    print(student.grades)
    print(student.test_results)

    print(student.get_subject_average_grade("Математика"))
    print(student.get_subject_average_grade("Физика"))

    print(student.get_overall_average_grade())


