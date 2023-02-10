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

    class Meta:
        verbose_name_plural = 'Descriptions'
    
    def __str__(self):
        return f"{self.text[:50]}..."

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)