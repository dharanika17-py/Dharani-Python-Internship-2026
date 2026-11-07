class ReportGenerator:

    def generate_report(self, student):
        result = "PASS" if all(
            mark >= 50 for mark in student.marks
        ) else "FAIL"

        performance = (
            "Good" if student.average >= 75
            else "Average" if student.average >= 50
            else "Needs Improvement"
        )

        print("\n----- STUDENT REPORT -----")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Department:", student.department)
        print("Average:", round(student.average, 2))
        print("Attendance:", student.attendance, "%")
        print("Result:", result)
        print("Performance:", performance)
        print("Status:", student.status)

    def generate_all_reports(self, students):
        if not students:
            print("No records available.")
            return

        for student in students:
            self.generate_report(student)