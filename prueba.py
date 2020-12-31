import uuid

class Student:

    name = ""
    last_name = ""
    id_student = 0
    total_students = 0

    def __init__(self, name, last_name):
        self.id_student += 1
        self.last_name = last_name
        self.name = name
        Student.total_students += 1

    def student_info(self):
        print("Identificador: {}\nname: {}".format(self.id_student, self.name))



students = ["rodrigo", "Elena", "Fidela"]
for student in students:
    student = Student(str(student), "urcino")
    print("Alumno: {} ".format(student.name), "Identificador: {}".format(student) )
    print("Tota de estudiantes: ",student.total_students)
