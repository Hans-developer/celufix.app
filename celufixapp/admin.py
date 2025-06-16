from django.contrib import admin
from .models import Marcas, Telefonos, Repuestos

# Register your models here.

admin.site.register(Marcas)
admin.site.register(Telefonos)
admin.site.register(Repuestos)
