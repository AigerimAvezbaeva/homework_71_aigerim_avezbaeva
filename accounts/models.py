from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class GenderChoices(TextChoices):
    MALE = 'male', 'Мужчина'
    FEMALE = 'female', 'Женщина'


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    account_info = models.CharField(
        max_length=100,
        verbose_name='Описание профиля',
        null=True,
        blank=True
    )
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        verbose_name='Пол',
        null=True,
        blank=True,
        max_length=20
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        null=True,
        blank=True,
        max_length=100)
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes')
    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='accounts.Account',
        related_name='subscribers')
    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
