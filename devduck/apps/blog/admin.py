from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import Course
from .models import Grid
from .models import Module
from .models import Post
from .models import ProgLanguage
from .models import Rating
from .models import Subjects

admin.site.register(Course)
admin.site.register(Grid)
admin.site.register(Module)
admin.site.register(Post)
admin.site.register(ProgLanguage)
admin.site.register(Rating)
admin.site.register(Subjects)