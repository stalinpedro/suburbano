from pyexpat import model
import graphene
from lineas.models import Linea, Estacion
from graphene_django import DjangoObjectType


class LineaType(DjangoObjectType):
    class Meta:
        model = Linea
        field = ("id", "nombre", "ubicacion", "estaciones")

class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion
        field = ("id", "nombre", "linea", "distancia_anterior")

class Query(graphene.ObjectType):
    lineas = graphene.List(LineaType)
    estaciones = graphene.List(EstacionType)

    def resolve_lineas(root,info):
        return Linea.objects.all()
    
    def resolve_estaciones(root,info):
        return Estacion.objects.all()

schema = graphene.Schema(query=Query)

