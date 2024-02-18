from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from module.models import Module
from module.pagination import ModulePagination
from module.serializers import ModuleSerializer
from users.permissions import IsModeratorPermission, IsTeacherPermission


class ModuleCreateAPIView(generics.CreateAPIView):
    """ Создание образовательного модуля """
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]


class ModulePublishedListAPIView(generics.ListAPIView):
    """ Вывод списка образовательных модулей для авторизованных пользователей (ограниченные данные) """
    serializer_class = ModuleSerializer
    pagination_class = ModulePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Module.objects.all()


class ModuleListAPIView(generics.ListAPIView):
    """ Вывод списка образовательных модулей (расширенные данные) """
    serializer_class = ModuleSerializer
    pagination_class = ModulePagination
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Module.objects.all()


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного образовательного модуля """
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if "moderator" in self.request.user.roles:
            return Module.objects.all()
        return Module.objects.filter(id_users=self.request.user)

    def get_object(self):
        data = super().get_object()
        data.count_view += 1
        data.save()
        return data


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """ Обновление образовательного модуля """
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Module.objects.all()


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """ Удаление образовательного модуля """
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Module.objects.all()
