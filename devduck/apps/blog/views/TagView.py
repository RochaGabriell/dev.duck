from django.views.generic.list import ListView

from devduck.apps.blog.models import Post
from devduck.apps.blog.models import Grid
from devduck.apps.blog.models import ProgLanguage


class TagLanguageView(ListView):

    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = ProgLanguage.objects.filter(id=self.kwargs['tag'])
        context['title'] = f'Postagens em {language[0].description}'
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(id_prog_language=self.kwargs['tag'])
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset


class TagSubjectsView(ListView):

    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grid = Grid.objects.filter(id_subject=self.kwargs['tag'])
        context['title'] = f'Postagens de {grid[0].id_subject}'
        return context

    def get_queryset(self):
        queryset_grid = Grid.objects.filter(id=self.kwargs['tag'])
        queryset = Post.objects.filter(id_grid=queryset_grid[0].id)
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset