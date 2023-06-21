from django.urls import path
from devduck.apps.core.views import RequestPermissionView, ListRequestPermissionView, ApproveRequestPermissionView, DisapproveRequestPermissionView

urlpatterns = [
    path('', RequestPermissionView.as_view(), name='request_permission'),
    path('list/', ListRequestPermissionView.as_view(), name='permission_list'),
    path('approve/<int:pk>/', ApproveRequestPermissionView.as_view(), name='approve_permission'),
    path('disapprove/<int:pk>/', DisapproveRequestPermissionView.as_view(), name='disapprove_permission'),
]