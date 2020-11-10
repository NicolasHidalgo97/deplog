from django import forms
from django.db import models
from .models import bitacora
from .models import encomienda


class BitacoraForm(forms.ModelForm):
    Nombre       = forms.CharField(
        widget = forms.TextInput(attrs={"placeholder":"Nombre empleado"})
        
        )
    Departamento = forms.IntegerField()
    Fecha        = forms.DateField()
    Hora         = forms.TimeField()
    Sumario      = forms.CharField(
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                "class": "new-class-name two",
                                "placeholder":"Descripción",
                                "id"   : "my-id-for-textareas",
                                "rows" : 10,
                                "cols" : 50,
                                }
                                ),
                            )
    class Meta:
        model  = bitacora
        fields = [
            'Nombre',
            'Departamento',
            'Fecha',
            'Hora',
            'Sumario'
        ]

class EncomiendaForm(forms.ModelForm):
    Nombre       = forms.CharField(
        widget = forms.TextInput(attrs={"placeholder":"Nombre empleado"})
        
        )
    Departamento = forms.IntegerField()
    Fecha        = forms.DateField()
    Hora         = forms.TimeField()
    Sumario      = forms.CharField(
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                "class": "new-class-name two",
                                "placeholder":"Descripción",
                                "id"   : "my-id-for-textareas",
                                "rows" : 10,
                                "cols" : 50,
                                }
                                ),
                            )
    Recibido     = models.BooleanField(default=False)
    Entregado    = models.BooleanField(default=False)
    class Meta:
        model  = encomienda
        fields = [
            'Nombre',
            'Departamento',
            'Fecha',
            'Hora',
            'Sumario',
            'Recibido',
            'Entregado',
        ]