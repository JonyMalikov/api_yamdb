from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken


def create_confirmation_code(user):
    return default_token_generator.make_token(user)


def send_confirmation_code(user, email):
    send_mail(
        subject='Код подтверждения для YaMDb',
        message=f'Ваш код подтверждения: {user.confirmation_code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


def create_token(user):
    return str(AccessToken.for_user(user))
