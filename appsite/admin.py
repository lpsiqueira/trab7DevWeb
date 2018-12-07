from django.contrib import admin
from .models import Language, Projeto

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['autor', 'nomeProjeto', 'linguagens']
    search_fields = ['autor']

admin.site.register(Projeto, ProjetoAdmin)

class LinguagemAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Language, LinguagemAdmin)