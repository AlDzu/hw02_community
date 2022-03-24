# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [

    # Главная страница
    path('', views.index, name='glang'),
    # Список постов после групп
    path('group/<slug>', views.group_posts, name='group'),
]
