from django.shortcuts import render, redirect
from .models import Poste

def cadastro_poste(request):
    if request.method == 'POST':
        # Salva dados iniciais na sessão
        request.session['problema'] = request.POST.get('problema')
        request.session['informacao'] = request.POST.get('informacao')
        return redirect('cadastro_poste:endereco_poste')

    return render(request, 'cadastro_poste/formulario.html')

def endereco_poste(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        problema = request.session.get('problema')
        informacao = request.session.get('informacao')

        # Cria o objeto Poste
        Poste.objects.create(
            problema=problema,
            informacao=informacao,
            cep=cep,
            rua=rua,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            estado=estado
        )

        # Limpa os dados da sessão, se desejar
        request.session.pop('problema', None)
        request.session.pop('informacao', None)

        return redirect('cadastro_poste:sucesso')

    # Se for GET, renderiza o formulário para preencher o endereço
    return render(request, 'cadastro_poste/endereco_poste.html')

def sucesso(request):
    return render(request, 'cadastro_poste/sucesso.html')
