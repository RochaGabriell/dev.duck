from django.urls import path
from devduck.apps.blog.views.HomeView import HomeView, RecentView
from devduck.apps.blog.views.NewPostView import NewPostView
from devduck.apps.blog.views.TagView import TagLanguageView, TagSubjectsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recent/', RecentView.as_view(), name='recent'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('t/languagem/<int:tag>/', TagLanguageView.as_view(), name='tag-language'),
    path('t/subject/<int:tag>/', TagSubjectsView.as_view(), name='tag-subjects'),
]