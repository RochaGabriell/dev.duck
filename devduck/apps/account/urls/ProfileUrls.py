from django.urls import path
from devduck.apps.account.views.ProfileView import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
    # path('edit/', ProfileEditView.as_view(), name='profile_edit'),
    # path('password/', PasswordChangeView.as_view(), name='password_change'),
]