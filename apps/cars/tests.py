from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from apps.cars.models import Car, Brand
from apps.cars.signal import car_pre_save


class CarPermissionTest(TestCase):

    def setUp(self):
        # 🔥 DESLIGA O SIGNAL (evita chamada da API)
        pre_save.disconnect(car_pre_save, sender=Car)

        # 👤 cria usuários
        self.user1 = User.objects.create_user(
            username='user1',
            password='123'
        )

        self.user2 = User.objects.create_user(
            username='user2',
            password='123'
        )

        # 🚗 cria marca
        self.brand = Brand.objects.create(name='VW')

        # 🚗 cria carro
        self.car = Car.objects.create(
            user=self.user1,
            brand=self.brand,
            model='Gol',
            factory_year=2020,
            model_year=2021,
            sale_price=30000,
            status='disponivel'
        )

    def tearDown(self):
        # 🔄 RELIGA O SIGNAL depois do teste
        pre_save.connect(car_pre_save, sender=Car)

    def test_owner_can_access_update(self):
        self.client.login(username='user1', password='123')

        response = self.client.get(
            reverse('car_update', args=[self.car.pk])
        )

        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_access_update(self):
        self.client.login(username='user2', password='123')

        response = self.client.get(
            reverse('car_update', args=[self.car.pk])
        )

        self.assertEqual(response.status_code, 404)

    def test_template_hides_edit_button_for_non_owner(self):
        self.client.login(username='user2', password='123')

        response = self.client.get(
            reverse('car_detail', args=[self.car.pk])
        )

        self.assertNotContains(response, 'Editar')