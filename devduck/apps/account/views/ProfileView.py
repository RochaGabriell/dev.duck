from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from devduck.apps.account.models import User
from devduck.apps.blog.models import Post


class ProfileView(ListView):

    model = Post
    template_name = 'profile/profile.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get('username')

        return context

    def get_queryset(self):
        posts = super().get_queryset()
        username = self.kwargs.get('username')

        if username:
            user = User.objects.get(username=username)
        else:
            user = self.request.user

        posts = Post.objects.filter(id_user=user.id)

        return posts
