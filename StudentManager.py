class StudentManager:
    def __init__(self, students=None):
        self.students = students if students is not None else []

    def add_student(self, student):
        if self.find_student(student.student_id):
            raise ValueError("Student ID already exists!")
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def view_students(self):
        return self.students

    def update_student(self, student_id, name, department, marks, attendance):
        student = self.find_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.update_details(name, department, marks, attendance)

    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        self.students.remove(student)