from django.db import models

# Create your models here.

class Marcas(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    imagenMarca = models.ImageField(upload_to='marcas', null=True)

    def __str__(self):
        return self.nombre


class Telefonos(models.Model):
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, related_name='telefonos')
    modelo = models.CharField(max_length=50, blank=False, null=False)
    parrafo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='telefonos')

    def __str__(self):
        return f'{self.marca} {self.modelo}'

class Repuestos(models.Model):
    telefono = models.ForeignKey(Telefonos, on_delete=models.CASCADE, related_name='repuestos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f'{self.telefono.marca} {self.nombre}'


