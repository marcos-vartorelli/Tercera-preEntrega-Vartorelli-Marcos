from django import forms

class AreaFormulario(forms.Form):
    nombre = forms.CharField()
    zona = forms.CharField()
    
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    

class ClienteFormulario(forms.Form):
    nombre_cliente = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    tipo_auto= forms.CharField()
    
    
class ProovedorFormulario(forms.Form):
    marca = forms.CharField()
    producto = forms.CharField()
    fechaDeEntrega = forms.DateField()
    