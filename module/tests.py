from rest_framework import status
from rest_framework.test import APITestCase
from module.models import Module
from users.models import User


class ModuleTestCase(APITestCase):
    """Тест модулей"""
    def setUp(self) -> None:
        """Создание тестовой привычки"""
        self.user = User.objects.create(
            email='test@test.com',
            password='testtesttest',
            is_superuser=True,
            is_staff=True,
        )

        self.data = Module.objects.create(title="Football", description="It's active",)
        self.client.force_authenticate(user=self.user)

    def test_create_module(self):
        """ Тестирование создания модуля """
        data = {
            "title": "test",
            "description": "test",
        }
        response = self.client.post('/module/create/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Module.objects.all().count(),
            2
        )

    def test_list_module(self):
        """ Тестирование вывода списка модулей """
        response = self.client.get('/module/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            User.objects.all().count(),
            1
        )

    def test_list_all_module(self):
        """ Тестирование вывода полных данных списка модулей """
        response = self.client.get('/module/all/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_module(self):
        """ Тестирование обновления данных о module """
        data = {"title": "test", }

        response = self.client.put(f'/module/update/{self.data.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], 'test')

    def test_delete_module(self):
        """ Тестирование удаления module """
        response = self.client.delete(f'/module/delete/{self.data.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
