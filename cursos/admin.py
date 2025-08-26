from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duracion", "plataforma", "dificultad")
    search_fields = ("nombre", "plataforma")
    list_filter = ("dificultad", "plataforma")
