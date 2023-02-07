from django.db import models

# Create your models here.
class ClassTopic(models.Model):
    class_name = models.CharField(max_length = 70)

    def __str__(self):
        return self.class_name