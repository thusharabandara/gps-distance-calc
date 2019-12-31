# import libraries
from django.urls import path
from . import views

# list of urls
urlpatterns = [
    path('calDistance', views.calDistance, name="calDistance"),
    path('', views.index, name='index')
]