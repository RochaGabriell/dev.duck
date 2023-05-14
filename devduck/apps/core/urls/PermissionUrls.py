from django.urls import path
from devduck.apps.core.views import RequestPermissionView

app_name = 'core'

urlpatterns = [
    path('', RequestPermissionView.as_view(), name='request_permission'),
]