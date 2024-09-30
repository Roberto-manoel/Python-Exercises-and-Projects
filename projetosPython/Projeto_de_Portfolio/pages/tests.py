from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
from pages import views

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_get_site(self):
        response = self.client.get(reverse('site'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_get_redes_sociais(self):
        response = self.client.get(reverse('redes_sociais'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/redes-sociais.html')

    @patch('requests.get')
    def test_get_tech_news(self, mock_get):
        mock_get.return_value.json.return_value = {'articles': []}
        response = self.client.get(reverse('tech_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/tech_news.html')
