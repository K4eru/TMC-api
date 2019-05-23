from django import forms
from .models import Cliente, Orden, Tecnico
from django.core.exceptions import ValidationError
from django.utils import timezone


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre","direccion","ciudad","comuna","telefono","correo"]

    def clean_nombre(self):
            nombre = self.cleaned_data['nombre']
            if len(nombre.split(' ')) < 4 :
                raise ValidationError("Ingrese su nombre de nuevo")
            return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.isalpha():
            raise ValidationError('El telefono no puede contener letras')
        elif len(telefono) <= 8:
            raise ValidationError("Ingresa un telefono con 9 digitos")
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data['correo']

        correo_base, proveedor = correo.split("@")
        dominio, extension = proveedor.split(".")
        return correo

class TecnicoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        
        model = Tecnico
        fields = ["nombre", "cliente","email","password"]

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre.split(' ')) < 4 :
            raise ValidationError("Por favor ingresa tu nombre completo")
        return nombre
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ["folio","cliente","fecha","descripcion","tecnico"]

    def clean_horaTermino(self):
        horaTermino = self.cleaned_data['horaTermino']
        horaInicio = self.cleaned_data['horaInicio']
        if horaTermino is timezone.now:
            raise ValidationError("safe")
        return horaTermino