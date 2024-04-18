from project_alchemy.crud.lessons import create_lesson
from project_alchemy.database import Session
from project_alchemy.models import Teacher, Lesson


def create_teacher(session, name, surname, email, password):
    new_teacher = Teacher(name=name, surname=surname, email=email, password=password)
    session.add(new_teacher)
    session.commit()
    print("Учитель успешно создан!")

    create_lesson_option = input("Хотите создать урок для этого учителя? (y/n): ")
    if create_lesson_option.lower() == 'y':
        subject = input("Введите предмет урока: ")
        date = input("Введите дату урока (ГГГГ-ММ-ДД): ")
        create_lesson(session, subject, date, new_teacher.teacher_id)
        print("Урок успешно создан!")
    else:
        print("Урок не создан.")


def get_teacher_by_id(session: Session,
                      teacher_id: int):
    """
    A method for getting information about a specific teacher by his ID,
    along with the lessons he conducts.
    :return: Teacher object with associated lessons or None if not found
    """
    teacher = session.query(Teacher).filter_by(teacher_id=teacher_id).one_or_none()

    if teacher is None:
        return None

    lessons = session.query(Lesson).filter_by(teacher_id=teacher_id).all()
    teacher.lessons = lessons

    return teacher


def update_teacher(
        session: Session,
        teacher_id: int,
        name: str = None,
        surname: str = None,
        email: str = None,
        password: str = None
):
    """
    A method for updating information about a specific teacher.
    :return: Updated teacher object or None if not found
    """
    teacher = get_teacher_by_id(session, teacher_id)
    if not teacher:
        return None

    if name:
        teacher.name = name
    if surname:
        teacher.surname = surname
    if email:
        teacher.email = email
    if password:
        teacher.password = password

    session.commit()
    return teacher


def delete_teacher(session: Session, teacher_id: int):
    """
    A method for deleting a teacher from the database.
    :return: True if deleted successfully, False otherwise
    """
    teacher = (
        session
        .query(Teacher)
        .filter(Teacher.teacher_id == teacher_id)
        .one()
    )

    session.delete(teacher)


def get_all_teachers(session: Session):
    """
    A method to get a list of all teachers.
    :return: List of all teacher objects
    """
    teachers = session.query(Teacher).all()

    return teachers


def get_teacher_by_credentials(session, name, password):
    return session.query(Teacher).filter_by(name=name, password=password).first()
