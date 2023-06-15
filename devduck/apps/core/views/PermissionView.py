from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View


class RequestPermissionView(LoginRequiredMixin, View):
   
    template_name = 'permission/permission.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)