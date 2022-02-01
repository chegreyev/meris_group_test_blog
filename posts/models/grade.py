from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable


class Grade(
    AbstractUUID,
    AbstractTimeTrackable,
    AbstractCreatedByTrackable,
    models.Model,
):
    is_liked = models.BooleanField(
        default=True,
    )
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name=_("Пост"),
        related_name="grades",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Оценка")
        verbose_name_plural = _("Оценки")