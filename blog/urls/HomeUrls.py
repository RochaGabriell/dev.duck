from django.urls import path
from blog.views.HomeView import HomeView
from blog.urls.NewPostUrls import NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
]