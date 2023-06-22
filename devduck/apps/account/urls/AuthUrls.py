from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from devduck.apps.account.views.AuthView import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='recover/recover.html',
        email_template_name='recover/password_reset_email.html',
        subject_template_name='recover/password_reset_subject.txt',
        success_url = reverse_lazy("home"),
    ), name='password_reset'),
    path('reset/<uidb64>[0-9A-Za-z_\-]/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name = 'recover/password_reset_confirm.html',
            success_url = reverse_lazy("login"),
        ), name='password_reset_confirm'),
]