from django.urls import path
from blog.views.HomeView import HomeView
from blog.views.DocsView import (
    AboutView, ContactView, EditorGuideView,
    TermsView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('editor_guide/', EditorGuideView.as_view(), name='editor-guide'),
    path('terms/', TermsView.as_view(), name='terms'),
]