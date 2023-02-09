from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=index), # when we leave it blank like '', this means we are setting up our own url
]