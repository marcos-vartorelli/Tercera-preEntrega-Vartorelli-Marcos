from django import forms

class AreaFormulario(forms.Form):
    nombre = forms.CharField()
    zona = forms.CharField()
    
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()