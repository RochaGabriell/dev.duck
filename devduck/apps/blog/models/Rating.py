from django.db import models
from django.utils.translation import gettext_lazy as _

from devduck.apps.account.models.User import User
from .Post import Post

class Rating(models.Model):
    id_user_rated = models.ForeignKey(
        User,
        verbose_name=_("usuário avaliador"),
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    id_post = models.ForeignKey(
        Post,
        verbose_name=_("Postagem"),
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    like = models.BooleanField(_("curtida"), default=False, blank=True)
    created_at = models.DateTimeField(_("criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("atualizado em"), auto_now=True)

    def __str__(self) -> str:
        return f'Avaliador: {self.id_user_rated} | Postagem: {self.id_post}'

    class Meta:
        verbose_name = _("avaliação")
        verbose_name_plural = _("avaliações")