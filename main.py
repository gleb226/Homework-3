class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    mark = 1
    def __init__(self, name):
        super().__init__(name, 13)

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name, 39)

    def give_mark(self, student, mark):
        print("Teacher gave grade to", student.name)
        student.mark = mark

me = Person("Hlieb", 13)

good_student = Student("Hlieb")
bad_student = Student("Stas")

my_teacher = Teacher("Olga")

my_teacher.give_mark(good_student, 11)
my_teacher.give_mark(bad_student, 6)

print(good_student.mark)
print(bad_student.mark)