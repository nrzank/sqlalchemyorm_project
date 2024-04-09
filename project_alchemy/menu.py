from project_alchemy.crud.student import get_student_by_id
from project_alchemy.database import Session
from project_alchemy.models import Teacher, Student, Lesson, TeacherLessons


def print_menu():
    print("\n=== Main Menu ===")
    print("1. Update Student Information")
    print("2. Get Lessons Information")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice


def update_student(
        session: Session,
        student_id: int,
        name: str = None,
        surname: str = None,
        email: str = None,
        password: str = None
):
    """
    A method for updating information about a specific student.
    :return: Updated student object or None if not found
    """
    student = get_student_by_id(session, student_id)
    if not student:
        return None

    if name:
        student.name = name
    if surname:
        student.surname = surname
    if email:
        student.email = email
    if password:
        student.password = password

    session.commit()
    return student


def get_lessons_info(session: Session):
    """
    A method to get information about lessons, students registered for each lesson,
    and the teacher conducting each lesson.
    :return: List of dictionaries containing lesson information
    """
    lessons_info = []

    lessons = session.query(Lesson).all()

    for lesson in lessons:
        lesson_dict = {
            'lesson_id': lesson.lesson_id,
            'subject': lesson.subject,
            'date': lesson.date,
            'teacher_name': f"{lesson.teachers.name} {lesson.teachers.surname}" if lesson.teachers else "Unknown",
            'students_registered': []
        }

        registered_students = session.query(Student).join(TeacherLessons).filter(TeacherLessons.lesson_id == lesson.lesson_id).all()
        for student in registered_students:
            lesson_dict['students_registered'].append(f"{student.name} {student.surname}")

        lessons_info.append(lesson_dict)

    return lessons_info


def main():
    session = Session()

    while True:
        choice = print_menu()

        if choice == '1':
            student_id = int(input("Enter student ID: "))
            name = input("Enter new name (leave empty to skip): ")
            surname = input("Enter new surname (leave empty to skip): ")
            email = input("Enter new email (leave empty to skip): ")
            password = input("Enter new password (leave empty to skip): ")
            updated_student = update_student(session, student_id, name, surname, email, password)
            if updated_student:
                print(f"Student {updated_student.name} {updated_student.surname} updated successfully!")
            else:
                print("Student not found!")

        elif choice == '2':
            lessons_info = get_lessons_info(session)
            for lesson in lessons_info:
                print(f"Lesson ID: {lesson['lesson_id']}")
                print(f"Subject: {lesson['subject']}")
                print(f"Date: {lesson['date']}")
                print(f"Teacher: {lesson['teacher_name']}")
                print("Students Registered:")
                for student in lesson['students_registered']:
                    print(f"- {student}")
                print("=" * 50)

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
