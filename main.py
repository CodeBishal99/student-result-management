from database import *

create_table()

while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))
        marks = float(input("Enter Marks: "))

        add_student(name, roll, marks)

    elif choice == "2":
        students = view_students()

        print("\nID\tName\tRoll\tMarks")

        for student in students:
            print(
                f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}"
            )

    elif choice == "3":
        roll = int(input("Enter Roll Number: "))

        student = search_student(roll)

        if student:
            print("\nStudent Found")
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Roll: {student[2]}")
            print(f"Marks: {student[3]}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter Roll Number: "))
        delete_student(roll)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")