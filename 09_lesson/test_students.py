"""
Тесты для работы с таблицей student через SQLAlchemy.
Тесты: добавление, изменение, удаление сущности.
Используется фикстура с yield для автоматической очистки данных.
"""
import pytest
from database import SessionLocal, Student


@pytest.fixture
def session():
    """Фикстура для создания сессии БД."""
    with SessionLocal() as session:
        yield session


def test_create_student(session):
    """
    Тест добавления студента.
    Создаём студента и проверяем, что он появился в БД.
    """
    test_user_id = 999999
    new_student = Student(
        user_id=test_user_id,
        level="beginner",
        education_form="full-time",
        subject_id=1
    )
    session.add(new_student)
    session.commit()

    student_in_db = session.query(Student).filter_by(
        user_id=test_user_id
    ).first()

    assert student_in_db is not None, "Студент не найден в БД"
    assert student_in_db.level == "beginner"
    assert student_in_db.education_form == "full-time"

    session.delete(student_in_db)
    session.commit()


def test_update_student(session):
    """
    Тест изменения студента.
    Создаём студента, меняем его данные и проверяем обновление.
    """
    test_user_id = 999998
    student = Student(
        user_id=test_user_id,
        level="intermediate",
        education_form="part-time",
        subject_id=2
    )
    session.add(student)
    session.commit()

    student.level = "advanced"
    student.education_form = "full-time"
    session.commit()

    updated_student = session.query(Student).filter_by(
        user_id=test_user_id
    ).first()

    assert updated_student is not None, "Обновлённый студент не найден"
    assert updated_student.level == "advanced"
    assert updated_student.education_form == "full-time"

    session.delete(updated_student)
    session.commit()


def test_delete_student(session):
    """
    Тест удаления студента.
    Создаём студента, удаляем его и проверяем, что он исчез из БД.
    """
    test_user_id = 999997
    student = Student(
        user_id=test_user_id,
        level="beginner",
        education_form="full-time",
        subject_id=3
    )
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted_student = session.query(Student).filter_by(
        user_id=test_user_id
    ).first()

    assert deleted_student is None, "Студент не был удалён из БД"
