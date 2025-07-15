from django.shortcuts import render, redirect, get_object_or_404
from .models import Manutencao
from cadastro_poste.models import Poste, Lampada
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ManutencaoForm
from django.http import HttpResponseForbidden


from django.db.models import Q


@login_required
def lista_manutencoes(request):
    busca = request.GET.get('busca', '')
    manutencoes = Manutencao.objects.all().order_by('-data_manutencao')

    if busca:
        manutencoes = manutencoes.filter(
            Q(poste__id__icontains=busca) |
            Q(lampada__id__icontains=busca) |
            Q(tipo__icontains=busca) |
            Q(descricao__icontains=busca) |
            Q(status__icontains=busca) |
            Q(responsavel__username__icontains=busca)
        )

    postes = Poste.objects.all()
    lampadas = Lampada.objects.all()

    context = {
        'manutencoes': manutencoes,
        'postes': postes,
        'lampadas': lampadas,
        'busca': busca,
    }
    return render(request, 'manutencao/lista.html', context)


@login_required
def criar_manutencao(request):
    tipos = Manutencao.TIPO_MANUTENCAO_CHOICES
    status_choices = Manutencao.STATUS_CHOICES
    postes = Poste.objects.all()
    lampadas = Lampada.objects.all()

    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.responsavel = request.user
            manutencao.save()
            messages.success(request, 'Manutenção cadastrada com sucesso.')
            return redirect('manutencao:lista_manutencoes')
    else:
        form = ManutencaoForm()

    context = {
        'form': form,
        'tipos': tipos,
        'status_choices': status_choices,
        'postes': postes,
        'lampadas': lampadas,
    }
    return render(request, 'manutencao/criar.html', context)


@login_required
def excluir_manutencao(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Você não tem permissão para excluir manutenções.")

    manutencao = get_object_or_404(Manutencao, id=id)
    if request.method == 'POST':
        manutencao.delete()
        return redirect('manutencao:lista_manutencoes')

    return redirect('manutencao:lista_manutencoes')


@login_required
def editar_manutencao(request, id):
    manutencao = get_object_or_404(Manutencao, pk=id)
    if request.method == 'POST':
        form = ManutencaoForm(request.POST, instance=manutencao)
        if form.is_valid():
            manutencao_atualizado = form.save(commit=False)
            # mantém responsável original
            manutencao_atualizado.responsavel = manutencao.responsavel
            manutencao_atualizado.save()
            return redirect('manutencao:lista_manutencoes')
    else:
        form = ManutencaoForm(instance=manutencao)
    postes = Poste.objects.all()
    lampadas = Lampada.objects.all()
    return render(request, 'manutencao/editar.html', {'form': form, 'postes': postes, 'lampadas': lampadas})
