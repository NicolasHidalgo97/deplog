from django.db import models

# Create your models here.
class bitacora(models.Model):
    Nombre      = models.CharField(max_length=120) 
    Fecha       = models.DateField()
    Hora        = models.TimeField()
    Información = models.TextField()