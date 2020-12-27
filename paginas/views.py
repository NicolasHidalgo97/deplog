from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home_view(request,*args, **kwargs): #*args, **kwargs
 # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "home.html",{})
    # En otro caso redireccionamos al login
    return redirect('/inicio-sesion')

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request,'nosotros.html')

def servicio(request,redirigir=""):
    
    if redirigir == "1":
        return redirect('error')

    return render(request,'servicio.html')

def contacto(request,nombre="",apellido=""):
    html = ""
    
    if  nombre and apellido:
        html += "<p>El nombre completo es:</p> "
        html += f"<h4>{nombre} {apellido}</h4>"

    elif nombre:
        html += "<p>El nombre es:</p> "
        html += f"<h4>{nombre}</h4>"





    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)