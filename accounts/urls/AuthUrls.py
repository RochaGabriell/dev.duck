from django.urls import path
from accounts.views.AuthView import (
    RegisterView, LoginView, LogoutView
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    # path('profile/password/', PasswordChangeView.as_view(), name='password_change'),
]