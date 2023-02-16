from distutils.command.upload import upload
from django.db import models
import uuid

# Create your models here.
class ClassName(models.Model):
    name = models.CharField(max_length = 70)

    def __str__(self):
        return self.name

class ClassNotes(models.Model):
    topic = models.ForeignKey(ClassName, on_delete = models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
    
    def __str__(self):
        return f"{self.description[:50]}..."
