from django.db import models
from django.contrib.auth import get_user_model
from apps.cars.models import Car
from apps.motorcycle.models import Motorcycle

User = get_user_model()


class Lead(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "Novo"
        CONTACTED = "contacted", "Contatado"
        NEGOTIATING = "negotiating", "Em negociação"
        CLOSED = "closed", "Fechado"
        LOST = "lost", "Perdido"

    # Controle interno
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_leads"
    )

    # Dados do cliente
    name = models.CharField(max_length=120, verbose_name="Nome")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    message = models.TextField(blank=True, null=True, verbose_name="Mensagem")

    # Veículo
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="leads"
    )
    motorcycle = models.ForeignKey(
        Motorcycle,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="leads"
    )

    # Funil
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Status"
    )

    # Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        vehicle = self.car or self.motorcycle
        return f"{self.name} - {vehicle}"