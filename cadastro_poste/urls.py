from django.urls import path
from . import views

app_name = 'cadastro_poste'

urlpatterns = [
    path('', views.cadastro_poste, name='cadastro_poste'),
    path('endereco/', views.endereco_poste, name='endereco_poste'),  
    path('sucesso/', views.sucesso, name='sucesso'),
]