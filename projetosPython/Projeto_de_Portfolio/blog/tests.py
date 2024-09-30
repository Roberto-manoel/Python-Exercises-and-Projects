from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Postagem, Comentario
from unittest import mock

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.postagem = Postagem.objects.create(titulo='Test Post', conteudo='Test Content', autor=self.user)
        self.comentario = Comentario.objects.create(conteudo='Test Comment', postagem=self.postagem, usuario=self.user)

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser2',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful registration

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect after logout

    def test_post_list_view(self):
        response = self.client.get(reverse('postagem_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('postagem_detail', args=[self.postagem.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Comment')

    # Mock the requests.get method to test get_youtube_videos view
    @mock.patch('requests.get')
    def get_test_youtube_videos_view(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': []}
        response = self.client.get(reverse('youtube_videos'))
        self.assertEqual(response.status_code, 200)
