"""
Клиент для работы с Yougile API v2.
"""
import requests


class YougileClient:
    """Клиент для API Yougile (раздел Projects)."""

    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self, api_token):
        """
        Инициализация клиента.

        Args:
            api_token: API ключ для авторизации.
        """
        self.api_token = api_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }

    def create_project(self, title, users):
        """
        Создать новый проект (POST /api-v2/projects).

        Args:
            title: Название проекта.
            users: Словарь пользователей {user_id: role}.

        Returns:
            Response объект.
        """
        data = {
            "title": title,
            "users": users
        }
        return requests.post(
            f"{self.BASE_URL}/projects",
            headers=self.headers,
            json=data
        )

    def get_project(self, project_id):
        """
        Получить информацию о проекте (GET /api-v2/projects/{id}).

        Args:
            project_id: ID проекта.

        Returns:
            Response объект.
        """
        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, data):
        """
        Обновить проект (PUT /api-v2/projects/{id}).

        Args:
            project_id: ID проекта.
            data: Словарь с данными для обновления.

        Returns:
            Response объект.
        """
        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json=data
        )
