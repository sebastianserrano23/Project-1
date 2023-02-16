from django.contrib import admin
from .models import ClassName, Description, Image

# Register your models here.
models = [ClassName, Description, Image]
for model in models:
    admin.site.register(model)