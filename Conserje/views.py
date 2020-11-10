from django.shortcuts import render

from .forms import BitacoraForm, EncomiendaForm

from .models import bitacora,encomienda
# Create your views here.
def crear_bitacora_vista(request):
    form = BitacoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BitacoraForm()
    
    context = {
        'form': form
    }
    return render(request, "conserje/bitacora.html",context) 

def crear_encomienda_vista(request):
    form = EncomiendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form =EncomiendaForm

    context = {
        'form': form
    }
    return render(request, "conserje/encomienda.html",context)