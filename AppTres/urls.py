from django.urls import path
from AppTres import views


urlpatterns = [
    path('',views.inicio),
    path('area',views.area, name='Area'),
    path('empleado',views.empleado, name='Empleado'),
    path('cliente',views.cliente, name='Cliente'),
    path('proovedor',views.proovedor, name='Proovedor'),
    
]
