"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from paginas.views import home_view
from Conserje.views import (crear_bitacora_vista,
                            crear_encomienda_vista,
                            crear_departamento_vista,
                            detalles_bitacora_vista,
                            detalles_encomienda_vista,
                            detalles_departamento_vista,
                            editar_bitacora_vista,
                            editar_encomienda_vista,
                            editar_departamento_vista,
                            borrar_bitacora_vista,
                            borrar_encomienda_vista,
                            borrar_departamento_vista,
                            lista_bitacora_vista,
                            lista_encomienda_vista,
                            lista_departamento_vista,
                            )

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', home_view),

    path('bitacora/', crear_bitacora_vista),
    path('bitacora/<int:id>/detalles/',detalles_bitacora_vista,name='detalles-bitacora'),
    path('bitacora/<int:id>/editar/',editar_bitacora_vista),
    path('bitacora/<int:id>/borrar/',borrar_bitacora_vista),
    path('bitacora/lista/',lista_bitacora_vista,name='lista-bitacora'),   

    path('encomienda/', crear_encomienda_vista),
    path('encomienda/<int:id>/detalles/',detalles_encomienda_vista,name='detalles-encomienda'),
    path('encomienda/<int:id>/editar/',editar_encomienda_vista),
    path('encomienda/<int:id>/borrar/',borrar_encomienda_vista),
    path('encomienda/lista/',lista_encomienda_vista,name='lista-encomienda'),

    path('departamento/', crear_departamento_vista),
    path('departamento/<int:id>/detalles/',detalles_departamento_vista,name='detalles-departamento'),
    path('departamento/<int:id>/editar/',editar_departamento_vista),
    path('departamento/<int:id>/borrar/',borrar_departamento_vista),
    path('departamento/lista/',lista_departamento_vista,name='lista-departamento'),
]
