from django import forms


class EstadioFormulario(forms.Form):
    direccion = forms.CharField(required=True)
    anioFund = forms.IntegerField()

class EquipoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    ciudad = forms.CharField(required=True)

class JugadorFormulario(forms.Form):
    apellido = forms.CharField(required=True)
    numero = forms.IntegerField(required=True)
    esBueno = forms.BooleanField(required=True)