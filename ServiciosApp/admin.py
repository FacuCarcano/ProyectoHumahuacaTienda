from django.contrib import admin
from .models import Servicio, CategoriaCatalogo
# Register your models here.

class CategoriaCatalogoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(CategoriaCatalogo, CategoriaCatalogoAdmin)
