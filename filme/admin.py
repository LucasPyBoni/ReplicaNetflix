from django.contrib import admin
from django.utils.text import camel_case_to_spaces

from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# criando campo de filves vistos no admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {"fields":("filmes_vistos",)})
)
UserAdmin.fieldsets = tuple(campos)


admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)