from project_alchemy.crud.grades import (
    get_grades_by_lesson,
    get_average_grade_by_student,
    create_grade
)
from project_alchemy.crud.teacher import (
    get_teacher_by_id,
    create_teacher
)
from project_alchemy.crud.student import (
    create_student
)
from project_alchemy.crud.lessons import (
    create_lesson
)
from project_alchemy.database import Session


def main_menu():

    while True:
        print("\n=== Main Menu ===")
        print("1. Get teacher by ID")
        print("2. Create teacher")
        print("3. Create student")
        print("4. Create lesson")
        print("5. Create grade")
        print("6. Get grades by lesson")
        print("7. Get average grade by student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            teacher_id = int(input("Enter teacher ID: "))
            session = Session()
            result = get_teacher_by_id(session, teacher_id)
            if result:
                print(f"Teacher Name: {result.name} {result.surname}")
                print("Lessons:")
                for lesson in result.lessons:
                    print(f"- {lesson.subject}")
            else:
                print("Teacher not found!")

        elif choice == "2":
            name = input("Enter teacher name: ")
            surname = input("Enter teacher surname: ")
            email = input("Enter teacher email: ")
            password = input("Enter teacher password: ")
            session = Session()
            create_teacher(session, name, surname, email, password)
            print("Teacher created successfully!")

        elif choice == "3":
            name = input("Enter student name: ")
            surname = input("Enter student surname: ")
            group = input("Enter student group: ")
            email = input("Enter student email: ")
            password = input("Enter student password: ")
            session = Session()
            create_student(session, name, surname, group, email, password)
            print("Student created successfully!")

        elif choice == "4":
            subject = input("Enter lesson subject: ")
            date = input("Enter lesson date (YYYY-MM-DD): ")
            teacher_id = int(input("Enter teacher ID for the lesson: "))
            session = Session()
            create_lesson(session, subject, date, teacher_id)
            print("Lesson created successfully!")

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            lesson_id = int(input("Enter lesson ID: "))
            grade_value = int(input("Enter grade value: "))
            comments = input("Enter comments for the grade: ")
            session = Session()
            create_grade(session, student_id, lesson_id, grade_value, comments)
            print("Grade created successfully!")

        elif choice == "6":
            lesson_id = int(input("Enter lesson ID: "))
            session = Session()
            result = get_grades_by_lesson(session, lesson_id)
            if result:
                for grade in result:
                    print(f"Student ID: {grade.student_id}, Grade: {grade.grade_value}")
            else:
                print("No grades found for this lesson!")

        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            session = Session()
            result = get_average_grade_by_student(session, student_id)
            if result:
                print(f"Average grade for student {student_id}: {result}")
            else:
                print("No grades found for this student!")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
