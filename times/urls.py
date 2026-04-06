from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_times, name='lista_times'),
    path('editar/<int:id>/', views.editar_time, name='editar_time'),
    path('excluir/<int:id>/', views.excluir_time, name='excluir_time'),
]