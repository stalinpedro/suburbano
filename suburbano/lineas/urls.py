from cgitb import lookup
from posixpath import basename
from django.urls import include, path
from lineas import views
from rest_framework import routers
from rest_framework_nested import routers
#from views import DomainViewSet, NameserverViewSet

router = routers.DefaultRouter()
router.register('lineas', views.LineaView)

lineas_router = routers.NestedDefaultRouter(router,'lineas',lookup='linea')
lineas_router.register('estaciones', views.ListaEstacionView, basename="linea-estaciones")

router.register('estaciones', views.EstacionView)
router.register('viajes', views.ViajeView)
router.register('pasajeros', views.PasajeroView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lineas_router.urls)),
]