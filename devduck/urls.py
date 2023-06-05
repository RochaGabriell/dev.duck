"""
URL configuration for devduck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from devduck.apps.core.views.DocsView import Custom404View, Custom500View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('devduck.apps.blog.urls.HomeUrls')),
    path('accounts/', include('devduck.apps.account.urls.AuthUrls')),
    path('profile/', include('devduck.apps.account.urls.ProfileUrls')),
    path('docs/', include('devduck.apps.core.urls.DocsUrls')),
    path('request_permission', include('devduck.apps.core.urls.PermissionUrls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = Custom404View.as_view()
handler500 = Custom500View.as_view()
