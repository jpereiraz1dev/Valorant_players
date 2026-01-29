from django.contrib import admin
from django.urls import path
from galeria.views import index,player

urlpatterns = [
    path('',index, name='index'),
    path('player/<int:player_id>',player, name='player'),
]