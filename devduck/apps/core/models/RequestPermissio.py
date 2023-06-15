from django.db import models
from django.utils.translation import gettext_lazy as _

from devduck.apps.account.models import User


class RequestPermissio(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user',
        null=False,
        blank=False,
    )
    user_permission = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_permission',
        verbose_name=_('User permission'),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        verbose_name = _('Solicitar permissão')
        verbose_name_plural = _('Solicitar permissão')

    def __str__(self):
        return self.user.email