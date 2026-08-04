"""
Тесты для API Yougile (раздел Projects).
Методы: POST, GET, PUT /api-v2/projects
"""
import pytest
from yougile_client import YougileClient


# ВАЖНО: Для запуска тестов необходимо:
# 1. Заменить 'YOUR_API_TOKEN_HERE' на реальный API токен Yougile
# 2. Заменить 'YOUR_USER_ID_HERE' на реальный ID пользователя (UUID)

API_TOKEN = "YOUR_API_TOKEN_HERE"
USER_ID = "YOUR_USER_ID_HERE"


@pytest.fixture
def client():
    """Фикстура для создания клиента API."""
    return YougileClient(API_TOKEN)


class TestProjectsPositive:
    """Позитивные тесты для методов работы с проектами."""

    def test_create_project_positive(self, client):
        """
        Позитивный тест: создание проекта.
        POST /api-v2/projects
        """
        # Данные для создания проекта
        project_title = "Тестовый проект Зайчика"
        users = {USER_ID: "admin"}

        # Создаём проект
        response = client.create_project(project_title, users)

        # Проверяем успешное создание
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: "
            f"{response.text}"
        )

        # Проверяем, что в ответе есть данные проекта
        project_data = response.json()
        assert "id" in project_data, "В ответе должен быть ID проекта"
        assert project_data["title"] == project_title, (
            f"Название не совпадает: {project_data['title']}"
        )

        # Сохраняем ID для последующих тестов (если нужно)
        self.project_id = project_data["id"]

    def test_get_project_positive(self, client):
        """
        Позитивный тест: получение информации о проекте.
        GET /api-v2/projects/{id}
        """
        # Сначала создаём проект, чтобы получить его ID
        create_response = client.create_project(
            "Проект для GET теста", {USER_ID: "admin"}
        )
        project_id = create_response.json()["id"]

        # Получаем информацию о проекте
        response = client.get_project(project_id)

        # Проверяем успешное получение
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: "
            f"{response.text}"
        )

        # Проверяем данные
        project_data = response.json()
        assert project_data["id"] == project_id, "ID проекта не совпадает"
        assert "title" in project_data, "В ответе должно быть название"

    def test_update_project_positive(self, client):
        """
        Позитивный тест: обновление проекта.
        PUT /api-v2/projects/{id}
        """
        # Создаём проект для обновления
        create_response = client.create_project(
            "Старое название", {USER_ID: "admin"}
        )
        project_id = create_response.json()["id"]

        # Обновляем проект
        new_title = "Обновлённое название проекта"
        response = client.update_project(project_id, {"title": new_title})

        # Проверяем успешное обновление
        assert response.status_code == 200, (
            f"Ожидали 200, получили {response.status_code}: "
            f"{response.text}"
        )

        # Проверяем, что проект действительно обновился
        updated_project = response.json()
        assert updated_project["title"] == new_title, (
            f"Название не обновилось: {updated_project['title']}"
        )


class TestProjectsNegative:
    """Негативные тесты для методов работы с проектами."""

    def test_create_project_negative_no_title(self, client):
        """
        Негативный тест: создание проекта без обязательного поля title.
        POST /api-v2/projects
        """
        # Пытаемся создать проект без title
        import requests
        response = requests.post(
            f"{client.BASE_URL}/projects",
            headers=client.headers,
            json={"users": {USER_ID: "admin"}}  # Нет поля title
        )

        # Проверяем, что получили ошибку
        assert response.status_code >= 400, (
            f"Ожидали ошибку (4xx), получили {response.status_code}"
        )

    def test_get_project_negative_invalid_id(self, client):
        """
        Негативный тест: получение проекта с невалидным ID.
        GET /api-v2/projects/{id}
        """
        # Пытаемся получить проект с несуществующим ID
        invalid_id = "00000000-0000-0000-0000-000000000000"
        response = client.get_project(invalid_id)

        # Проверяем, что получили ошибку
        assert response.status_code >= 400, (
            f"Ожидали ошибку (4xx), получили {response.status_code}"
        )

    def test_update_project_negative_invalid_id(self, client):
        """
        Негативный тест: обновление проекта с невалидным ID.
        PUT /api-v2/projects/{id}
        """
        # Пытаемся обновить несуществующий проект
        invalid_id = "00000000-0000-0000-0000-000000000000"
        response = client.update_project(
            invalid_id, {"title": "Новое название"}
        )

        # Проверяем, что получили ошибку
        assert response.status_code >= 400, (
            f"Ожидали ошибку (4xx), получили {response.status_code}"
        )
