class Student:
    number_of_students = 0

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name
        self._mark = 0
        Student.number_of_students += 1

    @classmethod
    def get_number_of_students(cls):
        return Student.number_of_students

    # @staticmethod
    # def is_mark(mark):
    #     for i in range(1, len(mark)):
    #
    @staticmethod
    def get_mark(mark):
        if 87 > mark <= 100:
            print("Отлично")
        elif 74 > mark <= 87:
            print("Хорошо")
        elif 61 > mark <= 74:
            print("Удов")
        else:
            print("Fail")
        return mark

    @property
    def mark(self):
        print("working getter")
        return self._mark

    @mark.setter
    def mark(self, mark):
        print("working setter")
        self._mark = mark

student_1 = Student("Nurik", "Shadmanov", 90)
student_2 = Student("Kutman", "Osunbekov", 87)
student_3 = Student("Nazir", "Nazirov", 100)
student_4 = Student("Ali", "Alipov", 74)
print(student_4.get_mark(85))
