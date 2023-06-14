from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic.list import ListView

from devduck.apps.blog.models import Post


class HomeView(ListView):

    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 22

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'DevDuck'
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset


class RecentView(ListView):

    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 22

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recentes - DevDuck'
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset