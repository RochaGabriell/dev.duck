from django.db import models
from django.utils.translation import gettext_lazy as _

from .Course import Course


class Module(models.Model):
    description = models.CharField(
        _("descrição"),
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        error_messages={'unique': _("Já existe um módulo com esse nome.")},
    )
    id_course = models.ForeignKey(
        Course,
        verbose_name=_("curso"),
        on_delete=models.CASCADE,
        related_name="modules",
    )
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = _("módulo")
        verbose_name_plural = _("módulos")