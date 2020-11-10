from django.db import models

# Create your models here.
class bitacora(models.Model):
    Nombre       = models.CharField(max_length=120) 
    Departamento = models.IntegerField()
    Fecha        = models.DateField()
    Hora         = models.TimeField()
    Sumario      = models.TextField()

class encomienda(models.Model):
    Nombre                = models.CharField(max_length=120) 
    Departamento          = models.IntegerField()
    Fecha                 = models.DateField()
    Hora                  = models.TimeField()
    Sumario               = models.TextField()
    Recibido              = models.BooleanField(default=False)
    Entregado             = models.BooleanField(default=False)