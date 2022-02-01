import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name=_("Уникальное поле"),
    )

    class Meta:
        abstract = True


class AbstractTimeTrackable(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата изменения')
    )

    class Meta:
        abstract = True
        ordering = ('created_at', 'updated_at')


class AbstractCreatedByTrackable(models.Model):
    created_by = models.ForeignKey(
        'users.User',
        verbose_name=_("Кем создан"),
        related_name="%(app_label)s_%(class)s_created_by",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
