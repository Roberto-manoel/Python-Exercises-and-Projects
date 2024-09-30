from django.db import models

class SolicitacaoServico(models.Model):
    SERVICOS_CHOICES = [
        ('portfolio', 'Portfólio'),
        ('blog', 'Blog'),
        ('site', 'Site'),
    ]

    nome_completo = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    servico = models.CharField(max_length=10, choices=SERVICOS_CHOICES)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo
