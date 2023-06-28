from typing import Any
from django import http
from django.http.request import HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse

from devduck.apps.account.models import User
from devduck.apps.account.forms.AuthForm import UserCreationForm


class LoginView(LoginView):

    template_name = 'auth/base.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return http.HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)


class LogoutView(LogoutView):

    template_name = 'home/home.html'


class RegisterView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'auth/cadastro.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return http.HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastre-se'
        return context

    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        return super().form_valid(form)