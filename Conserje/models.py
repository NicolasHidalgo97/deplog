from django.db import models
from django.urls import reverse

# Create your models here.
class departamento(models.Model):
    Numero       = models.IntegerField() 
    Propietario = models.CharField(max_length=100)
    Residente = models.CharField(max_length=100)
    def __str__(self):
        return "%i" % (self.Numero)
    def get_absolute_url(self):
        return reverse("detalles-departamento",kwargs = {"id": self.id})

        
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

