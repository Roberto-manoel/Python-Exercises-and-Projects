from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", storage=S3Boto3Storage(), blank=True)
