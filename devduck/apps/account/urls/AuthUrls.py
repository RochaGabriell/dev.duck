from django.urls import path
from devduck.apps.account.views.AuthView import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('recover/', PasswordChangeView.as_view(), name='password_change'),
]