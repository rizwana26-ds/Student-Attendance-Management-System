# Student Attendance Management System

students = []
attendance = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    students.append([student_id, name])
    attendance.append([])

    print("Student added successfully!")


def mark_attendance():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudents:")
    
    for i in range(len(students)):
        print(i + 1, ".", students[i][0], "-", students[i][1])

    choice = int(input("Select student number: "))
    index = choice - 1

    if index < 0 or index >= len(students):
        print("Invalid student number.")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        attendance[index].append("Present")
        print("Attendance marked as Present.")

    elif status == "A":
        attendance[index].append("Absent")
        print("Attendance marked as Absent.")

    else:
        print("Invalid attendance status.")


def view_records():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n----- Attendance Records -----")

    for i in range(len(students)):
        student_id = students[i][0]
        name = students[i][1]

        records = attendance[i]

        present = records.count("Present")
        absent = records.count("Absent")
        total = len(records)

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("\nStudent ID:", student_id)
        print("Name:", name)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance:", percentage, "%")
        print("Records:", records)


# Main program

while True:

    print("\n==============================")
    print(" STUDENT ATTENDANCE MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        view_records()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")