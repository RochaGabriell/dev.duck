from django.db import models
from django.utils.translation import gettext_lazy as _

from .ProgLanguage import ProgLanguage
from devduck.apps.account.models.User import User
from .Grid import Grid


class Post(models.Model):
    id_user = models.ForeignKey(
        User,
        verbose_name=_("usuário"),
        on_delete=models.CASCADE,
        related_name="posts",
    )
    id_prog_language = models.ForeignKey(
        ProgLanguage,
        verbose_name=_("linguagem de programação"),
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )
    id_grid = models.ForeignKey(
        Grid,
        verbose_name=_("grade"),
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(
        _("título"),
        max_length=150,
        null=False,
        blank=False,
        unique=False,
        error_messages={'unique': _("Já existe um post com esse título.")},
    )
    content = models.TextField(
        _("conteúdo"),
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)

    def __str__(self) -> str:
        return 'Criador: {} | Título: {}'.format(self.id_user, self.title)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")