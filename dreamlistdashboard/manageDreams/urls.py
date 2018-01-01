from django.urls import path

from . import views

app_name = 'manageDreams'
urlpatterns = [
    path('', views.index, name='manageDreams1'),
]
