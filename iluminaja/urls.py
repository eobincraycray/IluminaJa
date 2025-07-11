from django.contrib import admin
from django.urls import path
from cadastro_poste import views

app_name = 'cadastro_poste'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cadastrar_poste, name='formulario'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
