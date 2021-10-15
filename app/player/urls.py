from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('v1/post', views.PlayerViewSet.as_view(), name='API create player'),
    #path('v1/get_all', views.PlayerViewSet.as_view(), name='API get players'),
    path('v1/delete/<int:pk>/', views.PlayerViewSet.as_view(), name='API delete player')
]
