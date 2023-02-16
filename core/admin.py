from django.contrib import admin
from .models import ClassName, ClassNotes

# Register your models here.
models = [ClassName, ClassNotes]
for model in models:
    admin.site.register(model)