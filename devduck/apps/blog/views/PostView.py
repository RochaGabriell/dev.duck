from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from devduck.apps.blog.models import Post
from devduck.apps.account.models import User
from devduck.apps.blog.forms.PostForm import CreatePostForm, UpdatePostForm


class NewPostView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = CreatePostForm
    template_name = 'post/post.html'

    def get_success_url(self) -> str:
        return reverse_lazy('see_post', kwargs={'username': self.object.id_user.username, 'pk': self.object.id})

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.id_user != request.user:
            messages.error(request, "Você não tem permissão para excluir esta postagem.")
            return redirect('profile')
        return super().get(request, *args, **kwargs)


class UpdatePostView(LoginRequiredMixin, UpdateView):

    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.id_user != request.user:
            messages.error(request, "Você não tem permissão para editar esta postagem.")
            return redirect('profile')
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse_lazy('see_post', kwargs={'username': self.object.id_user.username, 'pk': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_post'] = Post.objects.get(id=self.kwargs['pk']).id
        return context


class SeePostView(DetailView):
    
    model = Post
    template_name = 'post/see_post.html'

    def get_queryset(self):
        queryset_user = get_object_or_404(User.objects.filter(username=self.kwargs['username']))
        queryset = Post.objects.filter(id=self.kwargs['pk'], id_user=queryset_user)

        return queryset