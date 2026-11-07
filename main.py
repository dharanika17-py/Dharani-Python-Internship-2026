from Student import Student
from StudentManager import StudentManager
from ReportGenerator import ReportGenerator
from FileManager import FileManager


def get_marks():
    while True:
        try:
            marks = [int(x.strip()) for x in input(
                "Enter 3 subject marks separated by commas: "
            ).split(",")]

            if len(marks) != 3:
                print("Enter exactly 3 marks.")
            elif any(mark < 0 or mark > 100 for mark in marks):
                print("Marks must be between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Enter valid numbers.")


def get_attendance():
    while True:
        try:
            attendance = float(input("Enter attendance percentage: "))

            if 0 <= attendance <= 100:
                return attendance

            print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Enter a valid percentage.")


file_manager = FileManager()
student_manager = StudentManager(file_manager.load_data())
report_generator = ReportGenerator()


while True:
    print("\n===== OOP STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Performance Report")
    print("7. Save Data")
    print("8. Exit")

    choice = input("Choose an option: ").strip()

    try:
        if choice == "1":
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            department = input("Enter Department: ").strip()

            if not student_id or not name or not department:
                raise ValueError("Fields cannot be empty.")

            marks = get_marks()
            attendance = get_attendance()

            student = Student(
                student_id, name, department, marks, attendance
            )

            student_manager.add_student(student)
            file_manager.save_data(student_manager.students)
            print("Student added successfully!")

        elif choice == "2":
            students = student_manager.view_students()

            if not students:
                print("No student records found.")

            for student in students:
                print("\nID:", student.student_id)
                print("Name:", student.name)
                print("Department:", student.department)
                print("Marks:", student.marks)
                print("Attendance:", student.attendance, "%")

        elif choice == "3":
            student_id = input("Enter Student ID: ").strip()
            student = student_manager.find_student(student_id)

            if student:
                report_generator.generate_report(student)
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter Student ID to update: ").strip()

            if not student_manager.find_student(student_id):
                raise ValueError("Student not found.")

            name = input("Enter new name: ").strip()
            department = input("Enter new department: ").strip()
            marks = get_marks()
            attendance = get_attendance()

            student_manager.update_student(
                student_id, name, department, marks, attendance
            )

            file_manager.save_data(student_manager.students)
            print("Student updated successfully!")

        elif choice == "5":
            student_id = input("Enter Student ID to delete: ").strip()
            student_manager.delete_student(student_id)

            file_manager.save_data(student_manager.students)
            print("Student deleted successfully!")

        elif choice == "6":
            report_generator.generate_all_reports(
                student_manager.students
            )

        elif choice == "7":
            file_manager.save_data(student_manager.students)

        elif choice == "8":
            file_manager.save_data(student_manager.students)
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")

    except ValueError as error:
        print("Error:", error)