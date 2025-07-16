from django.urls import path
from . import views

app_name = 'cadastro_poste'

urlpatterns = [
    path('', views.cadastro_poste, name='cadastro_poste'),
    path('endereco/', views.endereco_poste, name='endereco_poste'),  
    path('sucesso/', views.sucesso, name='sucesso'),
    path('lampadas/', views.lista_lampadas, name='lista_lampadas'),
    path('lampadas/adicionar/', views.adicionar_lampada, name='adicionar_lampada'),
    path('lampadas/<int:pk>/editar/', views.editar_lampada, name='editar_lampada'),
    path('lampadas/<int:pk>/excluir/', views.excluir_lampada, name='excluir_lampada'),
    path('lista_De_Postes/', views.lista_De_Postes, name='lista_poste'), 
    path('lampada-por-poste/<int:poste_id>/', views.lampada_por_poste, name='lampada_por_poste'),
]
