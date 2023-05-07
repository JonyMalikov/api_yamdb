from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Неверно введено имя'
            )]
    )
    email = models.EmailField(
        'email',
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        'name',
        blank=True,
        max_length=150
    )
    last_name = models.CharField(
        'last_name',
        blank=True,
        max_length=150
    )
    bio = models.TextField(
        'biography',
        blank=True,
        null=True
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        default=USER,
        max_length=50
    )

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR

    @property
    def is_admin(self):
        return self.role == User.ADMIN or self.is_superuser
