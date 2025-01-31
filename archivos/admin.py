from django.contrib import admin
from .models import ArchivoBinarioChangeName, ArchivosCatalogo, Notificacion, ArchivoUnico
from .forms import ArchivosCatalogoForm
# Register your models here.

class ArchivoUnicoAdmin(admin.ModelAdmin):
    list_display = ['archivoUnico']

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ['mensaje', 'subido']

class ArchivoBinarioChangeNameAdmin(admin.ModelAdmin):
    list_display = ['archivo', 'nombreAntiguo', 'offset0x3E0', 'subido_en']

class ArchivosCatalogoAdmin(admin.ModelAdmin):
    form = ArchivosCatalogoForm
    list_display = ['pk', 'archivo', 'subido_por', 'subido_en', 'publico']

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Solo establece el usuario al crear una nueva instancia
            try:
                obj.subido_por = request.user.username + " | " + request.user.email
            except:
                obj.subido_por = request.user.username 
        super().save_model(request, obj, form, change)
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si obj no es None, significa que se está editando una instancia existente
            return ['subido_por', 'subido_en']
        else:
            return []
admin.site.register(ArchivosCatalogo, ArchivosCatalogoAdmin)
admin.site.register(ArchivoBinarioChangeName, ArchivoBinarioChangeNameAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
admin.site.register(ArchivoUnico, ArchivoUnicoAdmin)
