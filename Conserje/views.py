from django.shortcuts import render, get_object_or_404, redirect

from .forms import BitacoraForm, EncomiendaForm

from .models import bitacora,encomienda
# Vistas para Bitacoras.
def crear_bitacora_vista(request):
    form = BitacoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BitacoraForm()
    
    context = {
        'form': form
    }
    return render(request, "conserje/bitacora.html",context) 

def detalles_bitacora_vista(request,id):
    obj = get_object_or_404(bitacora,id=id)

    context={
        "object": obj
    }
    return render(request,"conserje/detalles_bitacora.html",context)

def editar_bitacora_vista(request, id):
    obj = get_object_or_404(bitacora, id=id)
    form = BitacoraForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../detalles/')
    context = {
        'form': form
    }
    return render(request, "conserje/bitacora.html", context)
    
def borrar_bitacora_vista(request,id):
    obj = get_object_or_404(bitacora,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../lista/')
    context={
        "object": obj

    }
    return render(request,"Conserje/borrar_bitacora.html",context)

def lista_bitacora_vista(request):
    queryset = bitacora.objects.all()#lista de objetos
    context={
        "object_list" : queryset
    }
    return render(request,"conserje/bitacora_lista.html",context)

#Vistas para Encomiendas

def crear_encomienda_vista(request):
    form = EncomiendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form =EncomiendaForm

    context = {
        'form': form
    }
    return render(request, "conserje/encomienda.html",context)

def detalles_encomienda_vista(request,id):
    obj = get_object_or_404(encomienda,id=id)

    context={
        "object": obj
    }
    return render(request,"conserje/detalles_encomienda.html",context)

def editar_encomienda_vista(request, id):
    obj = get_object_or_404(encomienda, id=id)
    form = EncomiendaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../detalles/')
    context = {
        'form': form
    }
    return render(request, "conserje/encomienda.html", context)

def borrar_encomienda_vista(request,id):
    obj = get_object_or_404(encomienda,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../lista/')
    context={
        "object": obj

    }
    return render(request,"Conserje/borrar_encomienda.html",context)

def lista_encomienda_vista(request):
    queryset = encomienda.objects.all()#lista de objetos
    context={
        "object_list" : queryset
    }
    return render(request,"conserje/encomienda_lista.html",context)