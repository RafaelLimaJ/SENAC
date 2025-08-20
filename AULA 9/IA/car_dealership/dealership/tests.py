from django.test import TestCase
from .models import Car  # Assuming there is a Car model in models.py

class CarModelTest(TestCase):

    def setUp(self):
        Car.objects.create(make="Toyota", model="Corolla", year=2020)
        Car.objects.create(make="Honda", model="Civic", year=2021)

    def test_car_creation(self):
        toyota = Car.objects.get(make="Toyota")
        honda = Car.objects.get(make="Honda")
        self.assertEqual(toyota.model, "Corolla")
        self.assertEqual(honda.year, 2021)

    def test_car_str(self):
        car = Car(make="Ford", model="Mustang", year=2022)
        self.assertEqual(str(car), "Ford Mustang (2022)")  # Assuming __str__ method is defined in Car model