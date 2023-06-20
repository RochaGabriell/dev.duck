from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.db.models import Count

from devduck.apps.blog.models import Post, Rating


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
        posts_result = []
        result = Rating.objects.values('id_post').annotate(ratingPost=Count('like')).filter(like=True).order_by('-ratingPost')[:30]

        for num, obj in enumerate(result, 1):
            queryset.filter(id=obj['id_post'])
            consult = queryset.get(id=obj['id_post'])
            consult.rating = obj['ratingPost']
            consult.count = num
            posts_result.append(consult)

        return posts_result


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
        queryset = super().get_queryset().order_by('-created_at')

        for num, obj in enumerate(queryset, 1):
            obj.count = num
            obj.rating = Rating.objects.filter(id_post=obj.id, like=True).count()

        return queryset