from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')