from django.contrib import admin

from configuracoes.models import Parametro

# Register your models here.
admin.site.register(Parametro)

class DisplayAdmin(admin.ModelAdmin):
    list_display=['nome', 'valor']