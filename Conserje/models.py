from django.db import models
from django.urls import reverse

# Create your models here.
class bitacora(models.Model):
    Nombre       = models.CharField(max_length=120) 
    Departamento = models.IntegerField()
    Fecha        = models.DateField()
    Hora         = models.TimeField()
    Sumario      = models.TextField()
    def get_absolute_url(self):
        return reverse("detalles-bitacora",kwargs = {"id": self.id}) 


class encomienda(models.Model):
    Nombre                = models.CharField(max_length=120) 
    Departamento          = models.IntegerField()
    Fecha                 = models.DateField()
    Hora                  = models.TimeField()
    Sumario               = models.TextField()
    Recibido              = models.BooleanField(default=False)
    Entregado             = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("detalles-encomienda",kwargs = {"id": self.id}) 