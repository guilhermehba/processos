from django.contrib import admin
from processo.models import Gerencia, Macro, Processo



search_fields=['nome']
autocomplete_fields = ['nome']
admin.site.register(Gerencia)

class DisplayAdmin(admin.ModelAdmin):
    search_fields=['nome']
    list_display = ['nome','gerencia','status']
    list_display_links = ['nome','gerencia','status' ]

admin.site.register(Macro, DisplayAdmin)

class DisplayAdmin(admin.ModelAdmin):
    search_fields=['nome']
    list_display = ['nome','macro', 'descricao', 'processo', 'status', ]
    list_display_links = ['nome','macro', 'descricao', 'processo', 'status']

admin.site.register(Processo, DisplayAdmin)

admin.site.site_header = 'Administração do Caderno de Processos'



