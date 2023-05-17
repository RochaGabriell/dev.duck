from django.views.generic.detail import DetailView
from django.views.generic import ListView

from devduck.apps.account.models import User
from devduck.apps.blog.models import Post


class ProfileView(ListView):

    template_name = 'profile/profile.html'
    context_object_name = 'data_user'
    paginate_by = 3

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            user = User.objects.get(username=username)
        else:
            user = self.request.user

        return Post.objects.filter(id_user=user.id)
