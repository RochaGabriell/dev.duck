from django.views.generic.list import ListView
from django.contrib import messages

from devduck.apps.blog.models import Post, Grid, ProgLanguage, Rating


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

        if queryset.count() == 0:
            language = ProgLanguage.objects.filter(id=self.kwargs['tag'])
            messages.error(self.request, f'Não há postagens da linguagem de programação {language[0].description}.')

        for num, obj in enumerate(queryset, 1):
            obj.count = num
            obj.rating = Rating.objects.filter(id_post=obj.id, like=True).count()

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
        queryset = Post.objects.filter(id_grid=self.kwargs['tag'])

        if queryset.count() == 0:
            subject = Grid.objects.filter(id=self.kwargs['tag'])
            messages.error(self.request, f'Não há postagens da disciplina de {subject[0].id_subject}.')

        for num, obj in enumerate(queryset, 1):
            obj.count = num
            obj.rating = Rating.objects.filter(id_post=obj.id, like=True).count()

        return queryset