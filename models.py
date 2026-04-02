from sqlalchemy import Column, Integer, String, Float
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    surname = Column(String(100), nullable=False, comment="Фамилия")
    name = Column(String(100), nullable=False, comment="Имя")
    faculty = Column(String(100), nullable=False, comment="Факультет")
    course = Column(String(200), nullable=False, comment="Курс")
    grade = Column(Float, nullable=False, comment="Оценка")

    def __repr__(self):
        return (
            f"<Student(id={self.id}, surname='{self.surname}', "
            f"name='{self.name}', faculty='{self.faculty}', "
            f"course='{self.course}', grade={self.grade})>"
        )