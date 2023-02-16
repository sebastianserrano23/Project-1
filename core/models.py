from distutils.command.upload import upload
from django.db import models
import uuid

# Create your models here.
class ClassName(models.Model):
    name = models.CharField(max_length = 70)

    def __str__(self):
        return self.name

class Description(models.Model):
    topic = models.ForeignKey(ClassName, on_delete = models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.text[:50]}..."

class ImageUpload(models.Model):
    upload = models.ImageField(upload_to='uploads')