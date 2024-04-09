from project_alchemy.crud.grades import get_grades_by_lesson, get_average_grade_by_student
from project_alchemy.crud.teacher import get_teacher_by_id
from project_alchemy.database import Session


def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Get teacher by ID")
        print("2. Get grades by lesson")
        print("3. Get average grade by student")
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
            lesson_id = int(input("Enter lesson ID: "))
            session = Session()
            result = get_grades_by_lesson(session, lesson_id)
            if result:
                for grade in result:
                    print(f"Student ID: {grade.student_id}, Grade: {grade.grade_value}")
            else:
                print("No grades found for this lesson!")

        elif choice == "3":
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
