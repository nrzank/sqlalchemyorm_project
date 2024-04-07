from project_alchemy.database import Session
from project_alchemy.models import Lesson, Student, TeacherLessons


def create_lesson(
        session: Session,
        lesson_id: int,
        subject: str,
        date
):
    """
    A method for creating a new lesson.
    :return: Created lesson object
    """
    new_lesson = Lesson(
        lesson_id=lesson_id,
        subject=subject,
        date=date
    )
    session.add(new_lesson)
    session.commit()
    return new_lesson


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

        registered_students = session.query(Student) \
            .join(TeacherLessons) \
            .filter(TeacherLessons.lesson_id == lesson.lesson_id).all()

        for student in registered_students:
            lesson_dict['students_registered'].append(f"{student.name} {student.surname}")

        lessons_info.append(lesson_dict)

    return lessons_info


def update_lesson(session: Session,
                  lesson_id: int,
                  new_subject: str = None,
                  new_date: str = None):
    """
    A method for updating information about a specific lesson.
    :return: Updated lesson object or None if not found
    """
    lesson = session.query(Lesson).filter_by(lesson_id=lesson_id).one_or_none()

    if not lesson:
        return None

    if new_subject:
        lesson.subject = new_subject
    if new_date:
        lesson.date = new_date

    session.commit()
    return lesson


def delete_lesson(session: Session, lesson_id: int):
    """
    A method for deleting a lesson from the database.
    :return: True if the lesson was deleted successfully, False otherwise
    """
    lesson = session.query(Lesson).filter_by(lesson_id=lesson_id).one_or_none()

    if not lesson:
        return False

    session.delete(lesson)
    session.commit()
    return True
