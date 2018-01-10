from django.urls import path

from . import views

app_name = 'manageGifts'

urlpatterns = [
    path('add', views.add_gift, name='add_gift_new'),
    path('show', views.show_gift, name='show_all_gifts'),
    path('done', views.got_the_gift, name='delete_a_gift'),
    path('edit', views.edit_gift, name='edit_a_gift'),
]
