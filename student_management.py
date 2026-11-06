import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("File is empty or could not be read.")
        return []


def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        print("Records saved successfully!")
    except OSError:
        print("Error saving records.")


def get_marks():
    while True:
        try:
            marks = [int(x.strip()) for x in input(
                "Enter 3 subject marks separated by commas: "
            ).split(",")]

            if len(marks) != 3:
                print("Please enter exactly 3 marks.")
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


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(student_id):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()
    department = input("Enter Department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    marks = get_marks()
    attendance = get_attendance()

    student = {
        "id": student_id,
        "name": name,
        "department": department,
        "marks": marks,
        "attendance": attendance
    }

    students.append(student)
    save_students()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Marks:", student["marks"])
        print("Attendance:", student["attendance"], "%")


def search_student():
    student_id = input("Enter Student ID to search: ").strip()
    student = find_student(student_id)

    if student:
        print("\nStudent Found!")
        print(student)
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return

    print("Enter the new details:")
    name = input("Enter new name: ").strip()
    department = input("Enter new department: ").strip()

    if name:
        student["name"] = name
    if department:
        student["department"] = department

    student["marks"] = get_marks()
    student["attendance"] = get_attendance()

    save_students()
    print("Student updated successfully!")


def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    student = find_student(student_id)

    if student:
        students.remove(student)
        save_students()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def performance_report():
    if not students:
        print("No records available.")
        return

    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        result = "PASS" if all(
            mark >= 50 for mark in student["marks"]
        ) else "FAIL"

        print("\nName:", student["name"])
        print("Average Marks:", round(average, 2))
        print("Result:", result)


students = load_students()

while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Performance Report")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        performance_report()
    elif choice == "7":
        save_students()
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")