from rest_framework import status
from rest_framework.test import APITestCase
from category.models import Category
from users.models import User


class CategoryTestCase(APITestCase):
    def setUp(self) -> None:
        """ Тестовые данные """
        self.user = User.objects.create(
            email='test@example.com',
            password='testtesttest',
            is_superuser=True,
            is_staff=True,
        )
        self.client.force_authenticate(user=self.user)
        self.data = Category.objects.create(
            title="Art course",
            description="Develope",
        )

    def test_create_category(self):
        """ Создание категории """
        first_test = {
            "title": "Изобразительное искусство",
            "description": "Развивает креативное мышление.",
        }
        response = self.client.post('/category/create/', data=first_test)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            User.objects.all().count(),
            1
        )

    def test_list_category(self):
        """ Вывод списка категорий """
        data = {
            "title": "Art course",
            "description": "Develope"
        }
        response = self.client.get('/category/', data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Category.objects.all().count(),
            1
        )

    def test_retrieve_category(self):
        """ Вывод одного пользователя """
        response = self.client.get(f'/category/{self.data.pk}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            User.objects.all().count(),
            1
        )

    def test_update_category(self):
        """ Обновление данных о категории """
        data = {"title": "Art course1", "description": "Develope"}
        response = self.client.put(f'/category/update/{self.data.pk}/', data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["title"],
            'Art course1'
        )

    def test_delete_category(self):
        """ Тестирование удаления category """
        response = self.client.delete(f'/category/delete/{self.data.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
