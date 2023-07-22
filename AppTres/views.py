from django.http import HttpResponse
from django.shortcuts import render 
from AppTres.models import Area, Empleado, Cliente, Proovedor
from AppTres.forms import AreaFormulario, EmpleadoFormulario, ClienteFormulario, ProovedorFormulario


# Create your views here.

def inicio(request):
    return render(request,'AppTres/inicio.html')

def area(request):
    return render(request,'AppTres/area.html')

def empleado(request):
    return render(request,'AppTres/empleado.html')

#def cliente(request):
    #return render(request,'AppTres/cliente.html')

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
            
            empleado = Empleado(nombre = informacion['nombre'],apellido = informacion ['apellido'], email = informacion ['email'])
            empleado.save()
            return render(request,'AppTres/inicio.html')
    else:
        formulario = EmpleadoFormulario()
            
    return render(request,'AppTres/empleadoFormulario.html',{'Formulario': formulario})
       
       
def cliente(request):
    if request.method == 'POST':
        formulario = ClienteFormulario(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            cliente = Cliente(nombre_cliente = informacion['nombre_cliente'],
                                apellido = informacion ['apellido'],
                                email = informacion ['email'],
                                tipo_auto = ['auto'])
            cliente.save()
            return render(request,'AppTres/inicio.html')
    else:
        formulario = ClienteFormulario()
            
    return render(request,'AppTres/cliente.html',{'Formulario': formulario})

def proovedorForm(request):
    if request.method == 'POST':
        formulario = ProovedorFormulario(request.POST)
        print(formulario)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            proovedor = Proovedor(marca = informacion['marca'],
                                 producto = informacion ['producto'],
                                fechaDeEntrega = informacion ['fechaDeEntrega'])
            proovedor.save()
            return render(request,'AppTres/inicio.html')
    else:
        formulario = ProovedorFormulario()
            
    return render(request,'AppTres/proovedorFormulario.html',{'Formulario': formulario})


def busquedaCliente(request):
    return render(request, 'AppTres/busquedaCliente.html')


def buscar(request):
    
    if request.GET['nombre_cliente']:
        
        # respuesta = f"estoy buscando el cliente : {request.GET['nombre_cliente']}"
        nombre_cliente = request.GET['nombre_cliente']
        cliente = Cliente.objects.filter(nombre_cliente__icontains=nombre_cliente)
   
        return render(request, 'AppTres/inicio.html',{'nombre_cliente': nombre_cliente})
    
    else:
        
        respuesta = "no enviaste datos."
    
    #return HttpResponse(respuesta)
    return render(request, 'AppTres/inicio.html',{'respuesta': respuesta})

                                