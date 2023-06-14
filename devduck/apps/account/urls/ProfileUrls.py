from django.urls import path
from devduck.apps.account.views.ProfileView import ProfileView, ProfileEditView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('s/<str:username>/', ProfileView.as_view(), name='profile'),
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),
]