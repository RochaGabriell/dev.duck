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
        return render(request, template_name='docs/terms.html')


def handler404View(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500View(request):
    return render(request, 'errors/500.html', status=500)