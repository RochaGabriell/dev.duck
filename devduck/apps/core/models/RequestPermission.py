from django.db import models
from django.utils.translation import gettext_lazy as _

from devduck.apps.account.models import User


class RequestPermission(models.Model):
    requesting_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Usuário solicitante'),
        related_name='requested_permissions',
    )
    description = models.TextField(
        _("Descrição"),
        max_length=255,
        null=False,
        blank=False,
    )
    approved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='approved_permissions',
        verbose_name=_('Aprovado por'),
        null=True,
        blank=True,
    )
    is_approved = models.BooleanField(verbose_name=_('Aprovado'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado em'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado em'))

    class Meta:
        verbose_name = _('Solicitação de permissão')
        verbose_name_plural = _('Solicitações de permissão')

    def __str__(self):
        return f'{self.requesting_user}'