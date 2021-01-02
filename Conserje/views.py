from django.shortcuts import render, get_object_or_404, redirect
from .forms import BitacoraForm, EncomiendaForm, DepartamentoForm
from django.contrib.auth import authenticate
from .models import bitacora,encomienda,departamento

# Vistas para Bitacoras.
def crear_bitacora_vista(request):    
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    form = BitacoraForm(request.POST or None)
    if form.is_valid():
        b = form.save(commit=False)
        b.Nombre = request.user.username
        b.save()
        form = BitacoraForm()
    
    context = {
        'form': form
    }
    return render(request, "conserje/bitacora.html",context) 

def detalles_bitacora_vista(request,id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(bitacora,id=id)

    context={
        "object": obj
    }
    return render(request,"conserje/detalles_bitacora.html",context)

def editar_bitacora_vista(request, id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
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
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(bitacora,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../lista/')
    context={
        "object": obj

    }
    return render(request,"Conserje/borrar_bitacora.html",context)

def lista_bitacora_vista(request):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    queryset = bitacora.objects.all()#lista de objetos
    context={
        "object_list" : queryset
    }
    return render(request,"conserje/bitacora_lista.html",context)

#Vistas para Encomiendas

def crear_encomienda_vista(request):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    form = EncomiendaForm(request.POST or None)
    if form.is_valid():
        encomienda = form.save(commit=False)
        encomienda.Nombre = request.user.username
        encomienda.save()
        form = EncomiendaForm()

    context = {
        'form': form
    }
    return render(request, "conserje/encomienda.html",context)

def detalles_encomienda_vista(request,id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(encomienda,id=id)
    context={
        "object": obj
    }
    return render(request,"conserje/detalles_encomienda.html",context)

def editar_encomienda_vista(request, id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
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
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(encomienda,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../lista/')
    context={
        "object": obj

    }
    return render(request,"Conserje/borrar_encomienda.html",context)

def lista_encomienda_vista(request):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    queryset = encomienda.objects.all()#lista de objetos
    context={
        "object_list" : queryset
    }
    return render(request,"conserje/encomienda_lista.html",context)

    # Vistas para Departamentos.
def crear_departamento_vista(request):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DepartamentoForm()
    
    context = {
        'form': form
    }
    return render(request, "conserje/departamento.html",context) 

def detalles_departamento_vista(request,id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(departamento,id=id)

    context={
        "object": obj
    }
    return render(request,"conserje/detalles_departamento.html",context)

def editar_departamento_vista(request, id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(departamento, id=id)
    form = DepartamentoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../detalles/')
    context = {
        'form': form
    }
    return render(request, "conserje/departamento.html", context)
    
def borrar_departamento_vista(request,id):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    obj = get_object_or_404(departamento,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../lista/')
    context={
        "object": obj

    }
    return render(request,"conserje/borrar_departamento.html",context)

def lista_departamento_vista(request):
    if request.user.is_authenticated == False:
        return redirect("/inicio-sesion")
    queryset = departamento.objects.all()#lista de objetos
    context={
        "object_list" : queryset
    }
    return render(request,"conserje/departamento_lista.html",context)
