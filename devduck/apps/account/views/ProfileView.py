from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from devduck.apps.account.models import User
from devduck.apps.blog.models import Post


class ProfileView(ListView):

    model = Post
    template_name = 'profile/profile.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get('username')

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get('username')
        count = 0

        if username:
            user = User.objects.get(username=username)
        else:
            user = self.request.user

        queryset = Post.objects.filter(id_user=user.id)

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset
