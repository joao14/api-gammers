from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('create_player', views.PlayerViewSet.as_view(), name='Crear nuevo jugador')
]
