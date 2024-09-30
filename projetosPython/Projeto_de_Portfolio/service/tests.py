from django.test import TestCase, Client
from django.urls import reverse
from .models import SolicitacaoServico
from .forms import SolicitacaoServicoForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.solicitar_servico_url = reverse('solicitar-servico')  # Corrigido aqui

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'service/index.html')

    def test_solicitar_servico_GET(self):
        response = self.client.get(self.solicitar_servico_url)  # Corrigido aqui

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'service/solicitar_servico.html')

    def test_solicitar_servico_POST_add_new_servico(self):
        response = self.client.post(self.solicitar_servico_url, {  # Corrigido aqui
            'name': 'Test Service',
            'description': 'Test Description',
            # Add other fields here
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(SolicitacaoServico.objects.last().name, 'Test Service')
