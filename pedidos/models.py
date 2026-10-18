from django.db import models

# Create your models here.
class Pedido(models.Model):
    nombre = models.CharField()
    valor = models.DecimalField()
    estado = models.CharField()
    descripcion = models.TextField(max_length=100)
    registro = models.CharField(max_length=20)

def __str__(self):
    return self.nombre