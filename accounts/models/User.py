from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    matriculation = models.CharField(
        _("matrícula"),
        max_length=150,
        null=True,
        blank=False,
        unique=True,
        error_messages={'unique': _("Já existe um usuário com essa matrícula.")},
    )
    username = models.CharField(
        _("nome de usuário"),
        max_length=150,
        unique=True,
        blank=False,
        error_messages={'unique': _("Já existe um usuário com esse nome.")},
    )
    email = models.EmailField(
        _("endereço de email"),
        unique=True,
        blank=False,
        error_messages={'unique': _("Já existe um usuário com esse email.")},
    )
    is_staff = models.BooleanField(_("Equipe"), default=False)
    is_superuser = models.BooleanField(_("Super Usuário"), default=False)
    is_active = models.BooleanField(_("Ativo"), default=True)
    date_joined = models.DateTimeField(_("data de entrada"), auto_now_add=True)
    date_changed = models.DateTimeField(_("data de alteração"), auto_now=True)
    token = models.CharField(_("token"), max_length=150, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["matriculation", "email"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.matriculation

    class Meta:
        verbose_name = _("usuário")
        verbose_name_plural = _("usuários")