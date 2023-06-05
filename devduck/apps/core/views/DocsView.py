from django.shortcuts import render
from django.views.generic import View


class AboutView(View):

    def get(self, request):
        return render(request, template_name='docs/about.html', status=200)


class ContactView(View):

    def get(self, request):
        return render(request, template_name='docs/contact.html', status=200)


class EditorGuideView(View):

    def get(self, request):
        return render(request, template_name='docs/editor_guide.html', status=200)


class TermsView(View):

    def get(self, request):
        return render(request, template_name='docs/terms.html', status=200)


class Custom404View(View):
    def get(self, request, exception=None):
        context = {'error': '404'}
        return render(request, 'errors/error.html', context=context, status=404)


class Custom500View(View):
    def get(self, request):
        context = {'error': '500'}
        return render(request, 'errors/error.html', context=context, status=500)