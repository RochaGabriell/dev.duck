from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms.AuthForm import UserCreationForm, UserChangeForm
from devduck.apps.account.models.User import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = (
        "matriculation",
        "username",
        "email",
        "is_superuser",
        "is_active",
        "date_joined",
        "date_changed",
    )
    list_filter = (
        "matriculation",
        "username",
        "email",
        "is_active",
        "date_joined",
        "date_changed",
    )
    fieldsets = (
        ("Dados Usuário", {
            "fields": (
                "username",
                "matriculation",
                "password",
            )
        }),
        ("Contato", {
            "fields": (
                "email",
            )
        }),
        ("Permissões", {
            "fields": (
                "is_staff",
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
    )
    add_fieldsets = (
        ("Dados de Usuário", {
            "fields": (
                "username",
                "matriculation",
                "email",
            )
        }),
        ("Senha e Permissões", {
            "classes": ("wide", ),
            "fields": (
                "password1",
                "password2",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions",
            )
        }),
    )
    search_fields = ("matriculation", )
    ordering = ("matriculation", )


admin.site.register(User, UserAdmin)
