from .models import Orden, Cliente, Tecnico
from rest_framework import serializers



class ClienteSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = Cliente
        fields = ( 'nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'correo')

class TecnicoSerializer( serializers.HyperlinkedModelSerializer ):

    cliente = serializers.SlugRelatedField(
        many= True,
        read_only= True,
        slug_field='nombre'
    )

    class Meta:
        model = Tecnico
        fields = ( 'nombre', 'cliente', 'email', 'password' )


class OrdenSerializer( serializers.HyperlinkedModelSerializer ):

    # cliente = serializers.SlugRelatedField(
    #     many= False,
    #     read_only= True,
    #     slug_field='nombre'
    # )
    #
    # tecnico = serializers.SlugRelatedField(
    #     many= False,
    #     read_only= True,
    #     slug_field='nombre'
    # )

    class Meta:
        model = Orden
        fields = ( 'folio', 'cliente', 'fecha','descripcion', 'tecnico')