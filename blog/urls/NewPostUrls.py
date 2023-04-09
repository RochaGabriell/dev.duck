from django.urls import path
from blog.views.NewPostView import NewPostView

urlpatterns = [
    path('', NewPostView.as_view(), name='new_post')
]