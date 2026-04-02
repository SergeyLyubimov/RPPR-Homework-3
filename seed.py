from database import SessionLocal
from models import Student
import csv


def seed_data():
    with open('students.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        students_data = list(reader)
        students_data[0] = ['surname', 'name', 'faculty', 'course', 'grade']
        students_data = [dict(zip(students_data[0], v)) for v in students_data[1:]]

    session = SessionLocal()
    try:
        for data in students_data:
            student = Student(**data)
            session.add(student)
        session.commit()
        print(f"Добавлено {len(students_data)} записей.")

        all_students = session.query(Student).all()
        for s in all_students:
            print(s)
    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()