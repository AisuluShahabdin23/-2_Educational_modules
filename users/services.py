from django.conf import settings
from django.core.mail import send_mail


def welcome_send_mail(email=None):
    """ Отправка сообщения об успешной регистрации на почту """
    if email:
        send_mail(
            'Регистрация прошла успешно.',
            "Поздравляем с регистрацией!",
            settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
