from django.http import HttpResponse
from django.shortcuts import render 
from AppTres.models import Area, Empleado 
from AppTres.forms import AreaFormulario, EmpleadoFormulario


# Create your views here.

def inicio(request):
    return render(request,'AppTres/inicio.html')

def area(request):
    return render(request,'AppTres/area.html')

def empleado(request):
    return render(request,'AppTres/empleado.html')

def cliente(request):
    return render(request,'AppTres/cliente.html')

def proovedor(request):
    return render(request,'AppTres/proovedor.html')


def areaFormulario(request):
    if request.method == 'POST':
        formulario = AreaFormulario(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            area = Area(nombre=informacion['nombre'],zona=informacion['zona'])
            area.save()
            return render(request,'AppTres/inicio.html')
    else:
        formulario = AreaFormulario()
           
    return render(request,'AppTres/areaFormulario.html',{'Formulario': formulario})

def empleadoForm(request):
    if request.method == 'POST':
        formulario = EmpleadoFormulario(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            empleado = Empleado(nombre = informacion['nombre'],
                                apellido = informacion ['apellido'],
                                email = informacion ['email'])
            empleado.save()
            return render(request,'AppTres/inicio.html')
    else:
        formulario = EmpleadoFormulario()
            
    return render(request,'AppTres/empleadoFormulario.html',{'Formulario': formulario})
       
                                