from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from category.models import Category
from category.pagination import CategoryPagination
from category.serializers import CategorySerializer
from users.permissions import IsModeratorPermission, IsTeacherPermission


class CategoryCreateAPIView(generics.CreateAPIView):
    """ Создание категории """
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]


class CategoryListAPIView(generics.ListAPIView):
    """ Вывод списка образовательных модулей для авторизованных пользователей """
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного образовательного модуля """
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


class CategoryUpdateAPIView(generics.UpdateAPIView):
    """ Обновление образовательного модуля """
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Category.objects.all()


class CategoryDestroyAPIView(generics.DestroyAPIView):
    """ Удаление образовательного модуля """
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Category.objects.all()
