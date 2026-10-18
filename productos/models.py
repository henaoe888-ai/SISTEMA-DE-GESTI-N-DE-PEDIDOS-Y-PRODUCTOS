from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField()
    stock = models.PositiveIntegerField()
    registro = models.DateTimeField()

    def __str__(self):
        return self.nombre
