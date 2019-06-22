from django.db import models

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey

class Categoria(MPTTModel):
    nombre = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nombre']
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    """Model definition for Producto."""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="img")
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return self.nombre
