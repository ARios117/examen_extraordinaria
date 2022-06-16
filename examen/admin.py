from django.contrib import admin
from examen.models import Bicicleta, Alquiler, Cliente

# Register your models here.
admin.site.register(Bicicleta)
admin.site.register(Alquiler)
admin.site.register(Cliente)