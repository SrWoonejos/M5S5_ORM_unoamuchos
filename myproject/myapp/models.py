from django.db import models

# Modelo para la Empresa
class Empresa (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para el Producto
class Producto(models.Model):
    name = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name