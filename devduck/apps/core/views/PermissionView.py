from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponseBase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.models import Permission
from devduck.apps.core.models import RequestPermission
from devduck.apps.core.forms.RequestForm import RequestForm


class RequestPermissionView(LoginRequiredMixin, CreateView):

    model = RequestPermission
    form_class = RequestForm
    template_name = 'request/request.html'
    success_url = reverse_lazy('profile')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        if RequestPermission.objects.filter(requesting_user=request.user).exists():
            if RequestPermission.objects.get(requesting_user=request.user).is_approved == False:
                messages.error(request, 'Sua solicitação de permissão foi reprovada! Entre em contato com o administrador.')
                return redirect('profile')
            
            messages.error(request, 'Sua solicitação de permissão ainda não foi aprovada!')
            return redirect('profile')

        elif self.request.user.is_superuser or request.user.has_perm('blog.add_post'):
            messages.error(request, 'Você já possui permissão para postar!')
            return redirect('profile')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.requesting_user = self.request.user
        messages.success(self.request, 'Sua solicitação de permissão foi enviada com sucesso! Aguarde a aprovação do administrador.')
        return super().form_valid(form)
    

class ListRequestPermissionView(LoginRequiredMixin, ListView):

    model = RequestPermission
    template_name = 'request/list.html'
    context_object_name = 'requests'
    # paginate_by = 10


class ApproveRequestPermissionView(LoginRequiredMixin, View):

    def grant_permissions(self, user) -> None:
        grant_permissions = Permission.objects.filter(codename__in=['add_post', 'change_post', 'delete_post'])
        for permission in grant_permissions:
            user.user_permissions.add(permission)

    def get(self, request, pk):
        request_permission = RequestPermission.objects.get(pk=pk)
        request_permission.approved_by = request.user
        request_permission.is_approved = True
        request_permission.save()

        self.grant_permissions(request_permission.requesting_user)
        
        return redirect('permission_list')
    

class DisapproveRequestPermissionView(LoginRequiredMixin, View):

    def remove_permissions(self, user) -> None:
        remove_permissions = Permission.objects.filter(codename__in=['add_post', 'change_post', 'delete_post'])
        for permission in remove_permissions:
            user.user_permissions.remove(permission)

    def get(self, request, pk):
        request_permission = RequestPermission.objects.get(pk=pk)
        request_permission.approved_by = request.user
        request_permission.is_approved = False
        request_permission.save()

        self.remove_permissions(request_permission.requesting_user)

        return redirect('permission_list')