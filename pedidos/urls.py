from django.urls import path
from .import views

urlpatterns = [
    path("crear/",views.crear),
    path("listar/",views.listar),
    path("detalle/<int:id>/",views.detalle),
    path("editar/<int:id>/",views.editar),
    path("eliminar/<int:id>/",views.eliminar),
]