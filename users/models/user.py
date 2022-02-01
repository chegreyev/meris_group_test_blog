from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.models.managers import UserManager
from utils.models import AbstractUUID, AbstractTimeTrackable


class User(
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUUID,
    AbstractTimeTrackable
):
    first_name = models.CharField(
        max_length=128,
        verbose_name=_("Имя"),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=128,
        verbose_name=_("Фамилия"),
        blank=True,
        null=True,
    )
    patronymic = models.CharField(
        max_length=128,
        verbose_name=_("Отчество"),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        blank=True,
        null=True
    )
    username = models.CharField(
        verbose_name=_("Никнейм"),
        max_length=128,
        unique=True,
        blank=True,
        null=True,
    )
    follows = models.ManyToManyField(
        "users.User",
        related_name=_("my_subscribers"),
        verbose_name=_("Подписки"),
        blank=True,
    )
    subscribers = models.ManyToManyField(
        "users.User",
        related_name="my_followers",
        verbose_name=_("Подписчики"),
        blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
