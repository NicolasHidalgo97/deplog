from django.contrib import admin

# Register your models here.
from .models import bitacora, encomienda, departamento

admin.site.register(bitacora)
admin.site.register(encomienda)
admin.site.register(departamento)