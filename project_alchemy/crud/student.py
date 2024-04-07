from project_alchemy.database import Session
from project_alchemy.models import Student


def create_student(
        session: Session,
        name: str,
        surname: str,
        email: str,
        password: str
):
    """
    A method for creating a new student.
    :return: Created student object
    """

    new_student = Student(
        name=name,
        surname=surname,
        email=email,
        password=password
    )

    session.add(new_student)
    session.commit()
    return new_student


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


def delete_student(session: Session, student_id: int):
    """
    A method for deleting a student from the database.
    :return: True if deleted successfully, False otherwise
    """
    student = (
        session
        .query(Student)
        .filter(Student.student_id == student_id)
        .one_or_none()
    )

    if student:
        session.delete(student)
        session.commit()
        return True
    else:
        return False


def get_all_student(session: Session):
    """
    A method to get a list of all student.
    :return: List of all student objects
    """
    students = session.query(Student).all()

    return students
