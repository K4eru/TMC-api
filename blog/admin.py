from django.contrib import admin
from .models import Post,Cliente,Orden,Tecnico
from .forms import ClienteForm, TecnicoForm, OrdenForm

class AdminCliente(admin.ModelAdmin):
    list_display = ["__str__","nombre"]
    form = ClienteForm

class AdminTecnico(admin.ModelAdmin):
    list_display_tecnico = ["__str__"]
    form = TecnicoForm

class AdminOrden(admin.ModelAdmin):
    list_display_orden = ["__str__"]
    form = OrdenForm

admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Tecnico)