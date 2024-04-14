from datetime import datetime

from database import Session
from project_alchemy.crud.lessons import create_lesson
from project_alchemy.crud.teacher import create_teacher

with Session() as session:
    new_teacher = create_teacher(session=session, name='Nurzhan', surname='Kum', email='imcci', password='1234')
    session.add(new_teacher)
    session.commit()
    new_lesson = create_lesson(session=session, subject='Math', date=datetime.now())

    new_lesson.teachers.append(new_teacher)
    session.add(new_lesson)
    session.commit()
