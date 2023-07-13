from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render(request,'AppTres/Inicio.html')

def area(request):
    return render(request,'AppTres/area.html')

def empleado(request):
    return render(request,'AppTres/empleado.html')

def cliente(request):
    return render(request,'AppTres/cliente.html')

def proovedor(request):
    return render(request,'AppTres/proovedor.html')