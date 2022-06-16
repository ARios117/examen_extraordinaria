# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from examen.models import (Bicicleta, Alquiler, Cliente)
# from django.contrib.auth.models import User
from faker import Faker
# define STATIC_PATH in settings.py
# from proyecto.settings import STATIC_PATH
# from PIL import Image, ImageDraw, ImageFont
# from django.contrib.auth.hashers import make_password
from django.utils.dateparse import parse_date


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.cleanDataBase()   # clean database
        self.bicicleta()
        self.cliente()
        self.alquiler()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        Bicicleta.objects.all().delete()
        Alquiler.objects.all().delete()
        Cliente.objects.all().delete()

    def bicicleta(self):

        bicicleta = {}

        bicicleta[1] = {'id': 1001,
                    'tipo': 'urbana',
                    'anyoCompra': 2020,}
        bicicleta[2] = {'id': 1002,
                    'tipo': 'montaña',
                    'anyoCompra': 2021,}
        bicicleta[3] = {'id': 1003,
                    'tipo': 'eléctrica',
                    'anyoCompra': 2021,}

        for index, a in enumerate(bicicleta.values()):
            x = Bicicleta.objects.get_or_create(
                id=a['id'],
                tipo=a['tipo'],
                anyoCompra=a['anyoCompra']
            )[0]
            x.save()

    def cliente(self):

        cliente = {}

        cliente[1] = {'id': 1001,
                      'nombre': 'Frodo Bolsón',
                      'edad': 33, }
        cliente[2] = {'id': 1002,
                      'nombre': 'Samsagaz Gamyi',
                      'edad': 38, }
        cliente[3] = {'id': 1003,
                      'nombre': 'Peregrin Tuk',
                      'edad': 28}

        for index, a in enumerate(cliente.values()):
            x = Cliente.objects.get_or_create(
                id=a['id'],
                nombre=a['nombre'],
                edad=a['edad']
            )[0]
            x.save()

    def alquiler(self):

        alquiler = {}

        alquiler[1] = {'cliente': 1001,
                      'bicicleta': 1001,
                      'fecha': '2021-03-21', 
                      'horaComienzo': 9,
                      'horaFin': 19,}
        
        alquiler[2] = {'cliente': 1002,
                      'bicicleta': 1001,
                      'fecha': '2021-07-21', 
                      'horaComienzo': 10,
                      'horaFin': 22,}

        alquiler[3] = {'cliente': 1003,
                      'bicicleta': 1002,
                      'fecha': '2021-05-25', 
                      'horaComienzo': 8,
                      'horaFin': 20,}

        alquiler[4] = {'cliente': 1002,
                      'bicicleta': 1003,
                      'fecha': '2021-08-22', 
                      'horaComienzo': 12,
                      'horaFin': 15,}
        

        for index, a in enumerate(alquiler.values()):
            x = Alquiler.objects.get_or_create(
                bicicleta=Bicicleta.objects.get(id=int(a['bicicleta'])),
                cliente=Cliente.objects.get(id=int(a['cliente'])),
                fecha=a['fecha'],
                horaComienzo=a['horaComienzo'],
                horaFin=a['horaFin']
            )[0]
            x.save()