from django.urls import path
from devduck.apps.blog.views.HomeView import HomeView, RecentView
from devduck.apps.blog.views.PostView import NewPostView, DeletePostView, UpdatePostView, SeePostView, LikePostView
from devduck.apps.blog.views.TagView import TagLanguageView, TagSubjectsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recent/', RecentView.as_view(), name='recent'),

    path('<str:username>/<int:pk>/', SeePostView.as_view(), name='see_post'),
    path('post/new/', NewPostView.as_view(), name='new_post'),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name='edit_post'),
    path('post/like/<int:pk>/', LikePostView.as_view(), name='like_post'),

    path('t/languagem/<int:tag>/', TagLanguageView.as_view(), name='tag-language'),
    path('t/subject/<int:tag>/', TagSubjectsView.as_view(), name='tag-subjects'),
    
]