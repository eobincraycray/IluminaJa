from django.urls import path
from usuarios import views


app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:user_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil'),
]
