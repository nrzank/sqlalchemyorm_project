from sqlalchemy import func
from project_alchemy.database import Session
from project_alchemy.models import Grade


def create_grade(
        session: Session,
        grade_id: str,
        student_id: str,
        lesson_id: str,
        grade_value: str,
        comments: str = None
):
    """
    create the grade
    :return:
    """
    new_grade = Grade(
        grade_id=grade_id,
        student_id=student_id,
        lesson_id=lesson_id,
        grade_value=grade_value,
        comments=comments
    )
    session.add(new_grade)
    session.commit()

    return new_grade


def update_grade(
        session: Session,
        grade_id: int,
        new_grade_value: int = None,
        new_comments: str = None
):
    """
    A method for updating an existing grade entry.
    :return: Updated grade object or None if not found
    """

    grade = session.query(Grade).filter_by(grade_id=grade_id).first()

    if not grade:
        return None

    if new_grade_value is not None:
        grade.grade_value = new_grade_value
    if new_comments:
        grade.comments = new_comments

    session.commit()

    return grade


def get_grades_by_student(
        session: Session,
        student_id: int
):
    """
    A method for getting all grades for a specific student.
    :return: List of grades for the specified student or None if not found
    """

    grades = session.query(Grade).filter_by(student_id=student_id).all()

    if not grades:
        return None

    return grades


def get_grades_by_lesson(
        session: Session,
        lesson_id: int
):
    """
    A method for getting all grades for a specific lesson.
    :return: List of grades for the specified lesson or None if not found
    """

    grades = session.query(Grade).filter_by(lesson_id=lesson_id).all()

    if not grades:
        return None

    return grades


def get_average_grade_by_student(
        session: Session,
        student_id: int
):
    """
    A method for calculating a student's average grade.
    :return: Average grade for the specified student or None if not found
    """

    average_grade = session.query(func.avg(Grade.grade_value)) \
        .filter_by(student_id=student_id).scalar()

    if not average_grade:
        return None

    return average_grade
