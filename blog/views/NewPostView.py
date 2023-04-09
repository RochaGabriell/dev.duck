from django.shortcuts import render
from django.views.generic import View

class NewPostView(View):

    def get(self, request):
        return render(request, template_name='new_post/new_post.html', status=200)