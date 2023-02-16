from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    # home page
    path('', views.index, name = 'index')
]