from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image_url = models.URLField()