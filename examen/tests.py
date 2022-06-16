from django.test import TestCase, Client
from .models import Bicicleta, Alquiler, Cliente
from decimal import Decimal
from django.urls import reverse


class ExamenTest(TestCase):

    def setUp(self):
        self.bicicleta = {
            "id": 1001,
            "tipo": 'plegable',
            "anyoCompra": "2020"
        }
        self.cliente1 = {
            "id": 1001,
            "nombre": "Thorin",
            "edad": 195
        }
        self.cliente2 = {
            "id": 1002,
            "nombre": "Balin",
            "edad": 178
        }

    @classmethod
    def decode(cls, txt):
        return txt.decode("utf-8")

    def create_check(self, dictionary, ObjectClass):
        """ create an object of the class 'ObjectClass'
        using the dictionary. Then,
        check that all key-values in the
        dictionary are attributes in the object.
        return created object of class Object
        """
        # check that str function exists
        self.assertTrue(ObjectClass.__str__ is not object.__str__)
        # create object
        item = ObjectClass.objects.create(**dictionary)
        for key, value in dictionary.items():
            self.assertEqual(getattr(item, key), value)
        # execute __str__() so all the code in models.py is checked
        item.__str__()
        return item

    def test01(self):

        bicicleta = self.create_check(self.bicicleta, Bicicleta)
        cliente1 = self.create_check(self.cliente1, Cliente)
        cliente2 = self.create_check(self.cliente2, Cliente)

        self.alquiler1 = {'cliente': cliente1,
                      'bicicleta': bicicleta,
                      'fecha': '2021-11-08', 
                      'horaComienzo': 9,
                      'horaFin': 16,
                      }
        
        self.alquiler2 = {'cliente': cliente2,
                      'bicicleta': bicicleta,
                      'fecha': '2021-11-15', 
                      'horaComienzo': 10,
                      'horaFin': 22,
                      }

        alquiler1 = self.create_check(self.alquiler1, Alquiler)
        alquiler2 = self.create_check(self.alquiler2, Alquiler)

        response = self.client.get(
                reverse("lista_alquileres"),
                follow=True)
        response_txt = self.decode(response.content)
        self.assertFalse(response_txt.find("Nov. 8, 2021") == -1)