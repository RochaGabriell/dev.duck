from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from devduck.apps.account.forms.AuthForm import UserChangeForm
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
        queryset = queryset.order_by('-created_at')

        for obj in queryset:
            count += 1
            obj.count = count

        return queryset

class ProfileEditView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserChangeForm
    login_url = reverse_lazy('login')
    template_name = 'profile/editar.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form: UserChangeForm) -> HttpResponse:
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return super().form_valid(form)