from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('area', views.area, name='area'),
    path('empleado', views.empleado, name='empleado'),
    path('cliente', views.cliente, name='cliente'),
    path('proovedor', views.proovedor, name='proovedor'),
    path('AreaFormulario', views.areaFormulario, name= 'AreaFormulario'),
    path('EmpleadoFormulario', views.empleadoForm, name= 'EmpleadoFormulario'),
    #path('ClienteFormulario', views.clienteForm, name= 'ClienteFomulario'),
    path('ProovedorFormulario/', views.proovedorForm, name= 'ProovedorFormulario'),
    path('busquedaCliente', views.busquedaCliente, name= 'BusquedaCliente'),
    path('buscar/', views.buscar),
]
