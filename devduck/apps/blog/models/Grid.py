from django.db import models
from django.utils.translation import gettext_lazy as _

from .Module import Module
from .Subjects import Subjects


class Grid(models.Model):
    id_module = models.ForeignKey(
        Module,
        verbose_name=_("módulo"),
        on_delete=models.CASCADE,
        related_name="grids",
    )
    id_subject = models.ForeignKey(
        Subjects,
        verbose_name=_("disciplina"),
        on_delete=models.CASCADE,
        related_name="grids",
    )
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)

    def __str__(self) -> str:
        return f'{self.id_subject} | Modulo: {self.id_module}'

    class Meta:
        verbose_name = _("grade")
        verbose_name_plural = _("grades")