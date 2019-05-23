from django.contrib import admin
from .models import Post,Cliente,Orden,Tecnico

admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Tecnico)