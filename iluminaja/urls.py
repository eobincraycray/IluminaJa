from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.views.generic import RedirectView
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro_poste/', include('cadastro_poste.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('manutencao/', include('manutencao.urls')),
    path('', RedirectView.as_view(url='/cadastro_poste/', permanent=False)),

]
