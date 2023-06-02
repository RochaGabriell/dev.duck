from django.views.generic.list import ListView

from devduck.apps.blog.models import Post


class HomeView(ListView):

    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
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
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        count = 0

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset