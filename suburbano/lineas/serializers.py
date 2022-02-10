from lineas.models import Linea, Estacion, Pasajero, Viaje
from rest_framework import serializers


class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = ('nombre', 'ubicacion')


class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estacion
        fields = ('nombre', 'linea', 'distancia_anterior')


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ('nombre', 'apellidos',)


class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ('pasajero', 'fecha_inicio', 'estacion_inicio', 'fecha_final', 'estacion_final')
