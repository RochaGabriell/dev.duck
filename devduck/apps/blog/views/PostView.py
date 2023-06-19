from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from devduck.apps.blog.models import Post, Rating
from devduck.apps.account.models import User
from devduck.apps.blog.forms.PostForm import CreatePostForm, UpdatePostForm


class NewPostView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = CreatePostForm
    template_name = 'post/post.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Verifica se o usuário tem permissão para criar uma postagem
        if not request.user.has_perm('blog.add_post'):
            if not request.user.is_authenticated:
                return redirect('login')
            
            messages.error(request, "Você não tem permissão para criar uma postagem.")
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('see_post', kwargs={'username': self.object.id_user.username, 'pk': self.object.id})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.id_user = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Verifica se o usuário tem permissão para excluir a postagem ou se é o dono da postagem
        if not request.user.has_perm('blog.delete_post') or self.get_object().id_user != request.user:
            if not request.user.is_authenticated:
                return redirect('login')
            
            messages.error(request, "Você não tem permissão para excluir uma postagem.")
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)


class UpdatePostView(LoginRequiredMixin, UpdateView):

    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Verifica se o usuário tem permissão para editar a postagem ou se é o dono da postagem
        if not request.user.has_perm('blog.change_post') or self.get_object().id_user != request.user:
            if not request.user.is_authenticated:
                return redirect('login')
            
            messages.error(request, "Você não tem permissão para editar uma postagem.")
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self) -> str:
        username = self.object.id_user.username
        pk = self.object.id
        return reverse_lazy('see_post', kwargs={'username': username, 'pk': pk})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['id_post'] = Post.objects.get(id=self.kwargs['pk']).id
        return context


class SeePostView(DetailView):

    model = Post
    template_name = 'post/see_post.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset_user = get_object_or_404(User.objects.filter(username=self.kwargs['username']))
        queryset = Post.objects.filter(id=self.kwargs['pk'], id_user=queryset_user)
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['like'] = Rating.objects.filter(id_post=self.kwargs['pk'], like=True).count()
        return context
    

class LikePostView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        if Rating.objects.filter(id_post=self.kwargs['pk'], id_user_rated=request.user).exists():
            obj_rating = get_object_or_404(Rating.objects.filter(id_post=self.kwargs['pk'], id_user_rated=request.user))

            if obj_rating.like:
                obj_rating.like = False
            else:
                obj_rating.like = True

            obj_rating.save()

        else:
            obj_post = get_object_or_404(Post.objects.filter(id=self.kwargs['pk']))
            new_rating = Rating.objects.create(id_post=obj_post, id_user_rated=request.user, like=True)
            obj_rating = new_rating
        
        username = obj_rating.id_post.id_user.username
        
        return redirect('see_post', username=username, pk=self.kwargs['pk'])