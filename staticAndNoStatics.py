import uuid
class Student:

    total_students = 0
    id_studen = 0

    def __init__(self):
        self.id_studen = str(uuid.uuid4())[:6].upper()
        Student.total_students += 1

print("Primer estudiante")
rod = Student()
print("Identificador del estudiante: ", rod.id_studen)
print("Total de estudiantes registrados: ", rod.total_students)


print("\nSegundo estudiante")
elena = Student()
print("Identificador del estudiante: ", elena.id_studen)
print("Total de estudiantes registrados: ", elena.total_students)

print("\nOtro estudiante")
e1 = Student()
print("Identificador del estudiante: ", e1.id_studen)
print("Total de estudiantes registrados: ", e1.total_students)

print("\nOTro estudiante")
e2 = Student()
print("Identificador del estudiante: ", e2.id_studen)
print("Total de estudiantes registrados: ", e2.total_students)

