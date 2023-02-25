from django.core.validators import FileExtensionValidator
from django.db import models
from UserAccounts.models import UserAccount

# Create your models here.
class Notes(models.Model):
    topic = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    upload = models.ImageField(upload_to='notes/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description