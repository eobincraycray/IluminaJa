from django.urls import path
from . import views

app_name = 'manutencao'

urlpatterns = [
    path('', views.lista_manutencoes, name='lista_manutencoes'),
    path('criar/', views.criar_manutencao, name='criar_manutencao'),
    path('excluir/<int:id>/', views.excluir_manutencao, name='excluir_manutencao'),
    path('editar/<int:id>/', views.editar_manutencao, name='editar_manutencao'),
    path('registrar-correcao/', views.registrar_correcao, name='registrar_correcao'),
]
