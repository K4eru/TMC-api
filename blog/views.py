from django.shortcuts import render
from django.utils import timezone
from .models import Orden,Cliente,Tecnico
from rest_framework import viewsets
from .serializers import OrdenSerializer, ClienteSerializer, TecnicoSerializer



class OrdenesViewSet( viewsets.ModelViewSet ):
    queryset = Orden.objects.all().order_by( 'folio' )
    serializer_class = OrdenSerializer

class ClientesViewSet( viewsets.ModelViewSet ):
    queryset = Cliente.objects.all().order_by( 'nombre' )
    serializer_class = ClienteSerializer

class TecnicosViewSet( viewsets.ModelViewSet ):
    queryset = Tecnico.objects.all().order_by( 'nombre' )
    serializer_class = TecnicoSerializer