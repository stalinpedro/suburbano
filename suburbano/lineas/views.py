from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from lineas.serializers import LineaSerializer, EstacionSerializer, PasajeroSerializer, ViajeSerializer
from lineas.models import Linea, Estacion, Viaje, Pasajero
#from sesion05.suburbano.lineas import serializers

# Create your views here.
class LineaView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Linea.objects.all().order_by('id')
    serializer_class = LineaSerializer


class EstacionView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EstacionSerializer
    queryset = Estacion.objects.all().order_by('id')
    serializer_class = EstacionSerializer

class ListaEstacionView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Estacion.objects.filter(linea=self.kwargs['linea_pk'])

class PasajeroView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pasajero.objects.all().order_by('id')
    serializer_class = PasajeroSerializer


class ViajeView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Viaje.objects.all().order_by('id')
    serializer_class = ViajeSerializer
