
from django.contrib import admin
from .models import Dossier


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dossier, PostAdmin)