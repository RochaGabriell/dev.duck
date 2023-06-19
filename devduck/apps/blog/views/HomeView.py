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
        result = Rating.objects.values('id_post').annotate(ratingPost=Count('like')).filter(
            like=True).order_by('-ratingPost')
        count = 0

        posts_result = []

        for obj in result:
            for obj_post in queryset:
                if obj['id_post'] == obj_post.id:
                    obj_post.rating = obj['ratingPost']
                    posts_result.append(obj_post)

        for obj in posts_result:
            count += 1
            obj.count = count

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
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count
            obj.rating = Rating.objects.filter(id_post=obj.id, like=True).count()

        return queryset