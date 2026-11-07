class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, student_id, name, department, marks, attendance):
        super().__init__(name)
        self.__student_id = student_id
        self.__department = department
        self.__marks = marks
        self.__attendance = attendance
        self.__status = "Active"

    @property
    def student_id(self):
        return self.__student_id

    @property
    def department(self):
        return self.__department

    @property
    def marks(self):
        return self.__marks

    @property
    def attendance(self):
        return self.__attendance

    @property
    def status(self):
        return self.__status

    @property
    def average(self):
        return sum(self.__marks) / len(self.__marks)

    def update_details(self, name, department, marks, attendance):
        if name:
            self.name = name
        if department:
            self.__department = department
        self.__marks = marks
        self.__attendance = attendance

    def to_dict(self):
        return {
            "id": self.__student_id,
            "name": self.name,
            "department": self.__department,
            "marks": self.__marks,
            "attendance": self.__attendance,
            "status": self.__status
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            data["id"],
            data["name"],
            data["department"],
            data["marks"],
            data["attendance"]
        )
        student.__status = data.get("status", "Active")
        return student