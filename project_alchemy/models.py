from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, func, Text
)
from sqlalchemy.orm import relationship
from database import Base, engine


class Teacher(Base):
    """
    The Teachers table contains information about teachers.
    It is connected to the Lessons table through a many-to-Many
    (Many-to-Many) relationship through the teacher_lessons bundle table.
    It is linked to the Grade table through a One-to-Many relationship.
    """

    __tablename__ = 'Teachers'

    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime,
                        server_default=func
                        .timezone('UTC', func.now()))
    updated_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))
    lessons = relationship("Lesson", back_populates="teacher")

    lesson = relationship('Lesson',
                          uselist=False,
                          lazy="joined",
                          back_populates="Teachers",
                          secondary='teacher_lessons')

    grade = relationship('Grade',
                         uselist=False,
                         lazy="joined",
                         back_populates="Teachers"
                         )


class Student(Base):
    """
    The Students table contains information about students.
    Communications:
    It is linked to the Grade table through a One-to-Many relationship.
    """

    __tablename__ = 'Students'

    student_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    surname = Column(String(50), nullable=False)
    group = Column(String(255), default='group none')
    email = Column(String(50), unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))

    grade = relationship('Grade',
                         uselist=False,
                         lazy="joined",
                         back_populates="Students"
                         )


class Lesson(Base):
    """
    The Lessons table contains information about lessons.
    Communications:
    It is connected to the Teachers table through a many-to-Many (Many-to-Many)
    relationship through the teacher_lessons bundle table.
    It is linked to the Grade table through a One-to-Many relationship.
    """

    __tablename__ = 'lessons'

    lesson_id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    teacher = relationship("Teacher", back_populates="lessons")
    created_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))

    teachers = relationship('Teacher',
                            uselist=False,
                            lazy='joined',
                            back_populates='teacher_lessons')
    grade = relationship('Grade',
                         uselist=False,
                         lazy='joined',
                         back_populates='lessons')


class Grade(Base):
    """
    The Grade table contains information about student grades.
    Communications:
    It is linked to the Students table through a One-to-Many relationship.
    It is linked to the Lessons table through a One-to-Many relationship.
    """

    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Students.student_id'))
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    grade_value = Column(Integer, default='none grade')
    comments = Column(Text)
    created_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime,
                        server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))


class TeacherLessons(Base):
    """
    a table that links for many to many between Teacher and Lessons
    and stores the foreign key in itself
    """
    __tablename__ = 'teacher_lessons'

    teacher_id = Column(Integer, ForeignKey('Teachers.teacher_id'), primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'), primary_key=True)


Base.metadata.create_all(engine)
