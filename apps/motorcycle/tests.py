from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

from apps.motorcycle.models import Motorcycle, MotorcycleBrand

User = get_user_model()

class MotorcyclePermissionTest(TestCase):

    def setUp(self):
        # 🔥 FORÇA BRUTA: Desconecta todos os signals de pre_save do model Motorcycle
        # Isso evita que qualquer função de IA seja chamada, sem precisar do nome dela.
        pre_save.receivers = [] 

        # 👤 Criar usuários
        self.user1 = User.objects.create_user(username='user1', password='123')
        self.user2 = User.objects.create_user(username='user2', password='123')

        # 🏍️ Criar marca
        self.brand = MotorcycleBrand.objects.create(name='Kawasaki')

        # 🏍️ Criar moto vinculada ao user1
        self.moto = Motorcycle.objects.create(
            user=self.user1,
            brand=self.brand,
            model='Ninja H2R',
            factory_year=2024,
            model_year=2024,
            sale_price=150000,
            status='disponivel'
        )

    def test_owner_can_access_update(self):
        """Dono (user1) acessa a edição (Status 200)"""
        self.client.login(username='user1', password='123')
        response = self.client.get(reverse('motorcycle_update', args=[self.moto.pk]))
        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_access_update(self):
        """Não dono (user2) recebe 404"""
        self.client.login(username='user2', password='123')
        response = self.client.get(reverse('motorcycle_update', args=[self.moto.pk]))
        self.assertEqual(response.status_code, 404)

    def test_template_hides_edit_button_for_non_owner(self):
        """Botão editar não aparece para o user2 no detalhe da moto"""
        self.client.login(username='user2', password='123')
        response = self.client.get(reverse('motorcycle_detail', args=[self.moto.pk]))
        self.assertNotContains(response, 'Editar')