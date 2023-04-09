from django.urls import path
from blog.views.HomeView import HomeView
from blog.urls.NewPostUrls import NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]