from django.db import models
import os

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
         return self.nombre
    # eliminar imagenes de media cuando elimines el producto
    def delete(self, *args, **kwargs):
        # Guarda la referencia a la imagen antes de eliminar el objeto
        image_path = self.imagen.path if self.imagen else None
        
        # Llama al método delete del modelo para eliminar el objeto
        super(Producto, self).delete(*args, **kwargs)
        
        # Elimina la imagen del disco si existe
        if image_path and os.path.isfile(image_path):
            os.remove(image_path)

