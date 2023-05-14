from devduck.apps.blog.models import ProgLanguage, Grid, Module

def header_context(request):
    queryset_lang = ProgLanguage.objects.all()
    queryset_grid = Grid.objects.all()
    queryset_module = Module.objects.all()

    return {
        'language': queryset_lang,
        'grid': queryset_grid,
        'modules': queryset_module,
    }