from django.urls import path

from . import views

app_name = 'manageDreams'
urlpatterns = [
    path('add', views.post_dream, name='post_dream_new'),
    path('show', views.show_dream, name='show_all_dreams'),
]
