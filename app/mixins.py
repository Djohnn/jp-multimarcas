from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin(UserPassesTestMixin):
    """Garante acesso apenas ao dono do objeto (Update/Delete)"""
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user 
    
    
    def handle_no_permission(self):
        raise PermissionDenied("Você não tem permissão para acessarisso.")

class OwnerQuerySetMixin:
    """Isola os dados no nível da consulta ao banco"""

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class UserFormKwargsMixin:
    """Injeta o usuário logado nos argumentos do formulário"""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user 
        return kwargs