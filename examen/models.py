from django.template.defaultfilters import slugify
from django.db import models
from django.utils import timezone

# Create your models here.

class Bicicleta(models.Model):

    tipo = models.CharField(max_length=100)

    anyoCompra = models.IntegerField(default=0)

    class Meta:
        ordering = ['tipo', 'anyoCompra']

    def __str__(self):
        return self.tipo


class Cliente(models.Model):

    nombre = models.CharField(max_length=100)

    edad = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['nombre', 'edad']

    def save(self, *args, **kwargs):
        self.slug = slugify(
                (self.id)
            )

        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Alquiler(models.Model):

    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.SET_NULL, null=True, related_name='alquileres')

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name='alquileres')

    fecha = models.DateField(default=timezone.now())

    horaComienzo = models.IntegerField(default=0)

    horaFin = models.IntegerField(default=0)

    class Meta:
        ordering = ['bicicleta', 'cliente']

    def __str__(self):
        return 'Alquiler - %s, %s, %s, %s, %s,' % (self.bicicleta, self.cliente, self.fecha, self.horaComienzo, self.horaFin)