from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.pagination import UserPagination
from users.permissions import IsModeratorPermission, IsTeacherPermission
from users.serializers import UserSerializer, UserPublishedSerializer
from users.services import welcome_send_mail


class UsersCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        welcome_send_mail(email=request.data["email"])
        return self.create(request, *args, **kwargs)


class UserPublishedListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей для авторизованных пользователей (ограниченные данные) """
    serializer_class = UserPublishedSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей (расширенные данные) """
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return User.objects.all()


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод данных одного пользователя """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if 'moderator' in self.request.user.roles:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.pk)


class UsersUpdateAPIView(generics.UpdateAPIView):
    """ Обновление данных пользователя """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if 'moderator' in self.request.user.roles:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.pk)


class UsersDestroyAPIView(generics.DestroyAPIView):
    """ Удаление данных пользователя """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return User.objects.all()
