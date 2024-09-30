from django.test import TestCase, Client
from django.urls import reverse
from projects.models import Project

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.project_index_url = reverse('project_index')
        self.project1 = Project.objects.create(
            title='Test Project 1',
            description='Some random test project',
            # Add other necessary fields
        )
        self.project_detail_url = reverse('project_detail', args=[self.project1.id])

    def test_project_index_GET(self):
        response = self.client.get(self.project_index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_index.html')

    def test_project_detail_GET(self):
        response = self.client.get(self.project_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_detail.html')
