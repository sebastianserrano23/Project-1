from django.contrib import admin
from .models import ClassName, Description

# Register your models here.
models = [ClassName, Description]
for model in models:
    admin.site.register(model)