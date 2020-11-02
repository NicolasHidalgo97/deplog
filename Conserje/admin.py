from django.contrib import admin

# Register your models here.
from .models import bitacora, encomienda

admin.site.register(bitacora)
admin.site.register(encomienda)