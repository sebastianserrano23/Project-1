from django.contrib import admin
from .models import Notes

# Register your models here.
models = [Notes]
for model in models:
    admin.site.register(model)