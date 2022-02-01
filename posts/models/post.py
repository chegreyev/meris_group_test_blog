from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable


class Post(
    AbstractUUID,
    AbstractTimeTrackable,
    AbstractCreatedByTrackable,
    models.Model,
):
    name = models.CharField(
        verbose_name=_("Наименование"),
        max_length=128,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        max_length=128,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Пост")
        verbose_name_plural = _("Посты")

    @property
    def likes(self):
        return self.grades.filter(is_liked=True).count()

    @property
    def dislikes(self):
        return self.grades.filter(is_liked=False).count()
