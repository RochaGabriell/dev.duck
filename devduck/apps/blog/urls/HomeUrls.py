from django.urls import path
from devduck.apps.blog.views.HomeView import HomeView, RecentView
from devduck.apps.blog.views.NewPostView import NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recent/', RecentView.as_view(), name='recent'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
]