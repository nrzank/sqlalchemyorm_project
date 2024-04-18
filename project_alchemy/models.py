from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from sqlalchemy.orm import relationship, declarative_base

from project_alchemy.database import engine

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime, server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))

    lessons = relationship("Lesson", back_populates="teacher")
    students = relationship("Student", back_populates="teacher")


class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    surname = Column(String(50), nullable=False)
    group = Column(String(255), default='group none')
    email = Column(String(50), unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime, server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))

    grade = relationship('Grade', back_populates="student")
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'))
    teacher = relationship("Teacher", back_populates="students")


class Lesson(Base):
    __tablename__ = 'lessons'

    lesson_id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'))
    teacher = relationship("Teacher", back_populates="lessons")
    created_at = Column(DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime, server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))
    grade = relationship('Grade', back_populates="lesson")


class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.student_id'))
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    grade_value = Column(String, default='none grade')
    comments = Column(Text)
    created_at = Column(DateTime, server_default=func.timezone('UTC', func.now()))
    updated_at = Column(DateTime, server_default=func.timezone('UTC', func.now()),
                        onupdate=func.timezone('UTC', func.now()))

    student = relationship("Student", back_populates="grade")
    lesson = relationship("Lesson", back_populates="grade")


Base.metadata.create_all(engine)
