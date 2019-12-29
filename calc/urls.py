# import libraries
from django.urls import path
from . import views

# list of urls
urlpatterns = [
    path('', views.index, name='index')
]