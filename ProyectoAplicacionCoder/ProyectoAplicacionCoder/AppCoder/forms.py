from django import forms


class EstadioFormulario(forms.Form):
    direccion = forms.CharField(required=True)
    anioFund = forms.IntegerField()