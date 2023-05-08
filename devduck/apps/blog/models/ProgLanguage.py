from django.db import models
from django.utils.translation import gettext_lazy as _


class ProgLanguage(models.Model):
    description = models.CharField(
        _("descrição"),
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        error_messages={'unique': _("Já existe uma linguagem de programação com esse nome.")},
    )
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = _("linguagem de programação")
        verbose_name_plural = _("linguagens de programação")