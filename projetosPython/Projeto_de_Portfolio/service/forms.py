from django import forms
from django.core.exceptions import ValidationError
from .models import SolicitacaoServico
import re

def validate_nome_completo(value):
    if not re.match(r'^[a-zA-Z ]+$', value):
        raise ValidationError('Nome completo deve conter apenas letras e espaços.')

def validate_whatsapp(value):
    if not re.match(r'^\+?[1-9]\d{1,14}$', value):
        raise ValidationError('Número de Whatsapp inválido.')

class SolicitacaoServicoForm(forms.ModelForm):
    nome_completo = forms.CharField(validators=[validate_nome_completo])
    whatsapp = forms.CharField(validators=[validate_whatsapp])
    extra_info = forms.CharField(label='Informações extras', widget=forms.Textarea, required=False)

    class Meta:
        model = SolicitacaoServico
        fields = ['nome_completo', 'email', 'whatsapp', 'servico', 'extra_info']
