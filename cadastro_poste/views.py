from django.shortcuts import render, redirect
from .models import Poste

def cadastrar_poste(request):
    if request.method == 'POST':
        problema = request.POST.get('problema')
        informacao = request.POST.get('informacao')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        Poste.objects.create(
            problema=problema,
            informacao=informacao,
            latitude=latitude,
            longitude=longitude
        )
        return redirect('cadastro_poste:sucesso')  # ou para onde você quiser

    return render(request, 'cadastro_poste/formulario.html')

def sucesso(request):
    return render(request, 'cadastro_poste/sucesso.html')