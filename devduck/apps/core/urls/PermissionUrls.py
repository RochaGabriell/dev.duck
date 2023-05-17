from django.urls import path
from devduck.apps.core.views import RequestPermissionView

urlpatterns = [
    path('', RequestPermissionView.as_view(), name='request_permission'),
]