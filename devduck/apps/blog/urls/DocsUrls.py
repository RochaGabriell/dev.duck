from django.urls import path
from devduck.apps.blog.views.DocsView import (
    AboutView, ContactView, EditorGuideView,
    TermsView
)

app_name = 'docs'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('editor-guide/', EditorGuideView.as_view(), name='editor_guide'),
    path('terms/', TermsView.as_view(), name='terms'),
]