from shlex import join

from project_alchemy.database import Session
from project_alchemy.models import Student, Lesson, Grade


def create_student(session,
                   name,
                   surname,
                   group,
                   email,
                   password):
    new_student = Student(name=name,
                          surname=surname,
                          group=group,
                          email=email,
                          password=password)
    session.add(new_student)
    session.commit()
    return create_student


def get_student_by_id(
        session: Session,
        student_id: int
):
    """
    A method for getting information about a specific student by his ID.
    :return: student object or None if not found
    """

    get_student = session.query(Student).filter(Student.student_id == student_id).one_or_none()

    return get_student


#
# def update_student(
#         session: Session,
#         student_id: int,
#         name: str = None,
#         surname: str = None,
#         email: str = None,
#         password: str = None
# ):
#     """
#     A method for updating information about a specific student.
#     :return: Updated student object or None if not found
#     """
#     student = get_student_by_id(session, student_id)
#     if not student:
#         return None
#
#     if name:
#         student.name = name
#     if surname:
#         student.surname = surname
#     if email:
#         student.email = email
#     if password:
#         student.password = password
#
#     session.commit()
#     return student
#

def get_grades_all(session):
    """
       Получить оценки всех студентов из базы данных.
       :return: Список объектов оценок всех студентов.
       """

    return session.query(Grade).all()


# def delete_student(session: Session, student_id: int):
#     """
#     A method for deleting a student from the database.
#     :return: True if deleted successfully, False otherwise
#     """
#     student = (
#         session
#         .query(Student)
#         .filter(Student.student_id == student_id)
#         .one_or_none()
#     )
#
#     if student:
#         session.delete(student)
#         session.commit()
#         return True
#     else:
#         return False


def get_all_student(session: Session):
    """
    A method to get a list of all student.
    :return: List of all student objects
    """
    students = session.query(Student).all()

    return students


def get_student_by_credentials(session, name, password):
    return session.query(Student).filter_by(name=name, password=password).first()


def get_lessons_by_student(session, student_id):
    """
    Возвращает список уроков по ID студента.

    :param session: Сессия базы данных
    :param student_id: ID студента
    :return: Список уроков
    """
    lesson_grade_join = join(Lesson, Grade, Lesson.lesson_id == Grade.lesson_id)

    lessons = session.query(Lesson). \
        join(lesson_grade_join). \
        filter(Grade.student_id == student_id). \
        distinct(Lesson.lesson_id).all()

    return lessons


def get_grades_by_student(session, student_id):
    """
    Возвращает список оценок по ID студента.

    :param session: Сессия базы данных
    :param student_id: ID студента
    :return: Список оценок
    """
    grades = session.query(Grade).filter_by(student_id=student_id).all()
    return grades
