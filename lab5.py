class Student():
    def __init__(self, full_name, student_id, grades=None):
        self._full_name = full_name
        self._student_id = student_id
        self._grades = grades if grades is not None else []

    def __del__(self):

        print(f"Студента {self._full_name} видалено з пам'яті.")


    def get_full_name(self):
        return self._full_name

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_grades(self):
        return self._grades

    def add_grade(self, grade):
        self._grades.append(grade)

    def calculate_average_grade(self):
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def display_info(self):
        avg = self.calculate_average_grade()
        print(f"ID: {self._student_id} | ПІБ: {self._full_name} | Оцінки: {self._grades} | Середній бал: {avg:.2f}")


class Group:
    def __init__(self, group_name):
        self._group_name = group_name
        self._students = []

    def __del__(self):
        print(f" Групу {self._group_name} розформовано.")

    def get_group_name(self):
        return self._group_name

    def add_student(self, student):
        self._students.append(student)
        print(f"Студента {student.get_full_name()} додано до групи {self._group_name}.")

    def remove_student(self, student_id):
        for student in self._students:
            if student.get_student_id() == student_id:
                self._students.remove(student)
                print(f"Студента з ID {student_id} видалено з групи {self._group_name}.")
                return True
        print(f"Студента з ID {student_id} не знайдено в групі.")
        return False

    def display_rating(self):
        print(f"\n--- Рейтинг групи {self._group_name} ---")
        if not self._students:
            print("Група порожня.")
            return


        sorted_students = sorted(
            self._students, 
            key=lambda s: s.calculate_average_grade(), 
            reverse=True
        )

        for index, student in enumerate(sorted_students, start=1):
            print(f"{index}. ", end="")
            student.display_info()
        print("-" * 35)





student1 = Student("Коваленко Максим", "KV-31", [85, 90, 92, 88])
student2 = Student("Петренко Ірина", "KV-32", [95, 96, 92, 98])
student3 = Student("Сидоренко Олег", "KV-33", [70, 75, 80, 78])

group = Group("ІКТ-11")


group.add_student(student1)
group.add_student(student2)
group.add_student(student3)


group.display_rating()

student3.add_grade(85)
print(f"\nОновлено оцінки для {student3.get_full_name()}. Новий середній бал: {student3.calculate_average_grade():.2f}")


group.remove_student("KV-33")


group.display_rating()