from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView
from django.urls import reverse_lazy

from devduck.apps.blog.models import Post
from devduck.apps.blog.forms.NewPostForm import CreatePostForm


class NewPostView(LoginRequiredMixin, CreateView):
    
    model = Post
    form_class = CreatePostForm
    template_name = 'new_post/new_post.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        return super().form_valid(form)
