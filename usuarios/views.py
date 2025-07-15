from django.shortcuts import render
from usuarios.models import PerfilUsuario
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from usuarios.models import PerfilUsuario


User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')

            return render(request, 'contas/login.html')

        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('usuarios:lista_usuarios')

        else:
            messages.error(request, 'Senha incorreta.')

            return render(request, 'contas/login.html')

    return render(request, 'contas/login.html')


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('usuarios:cadastro')

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )
        usuario.save()
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('usuarios:login')

    return render(request, 'contas/cadastro.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('usuarios:login')


def lista_usuarios(request):
    busca = request.GET.get('busca', '')
    if busca:
        usuarios = User.objects.filter(
            Q(first_name__icontains=busca) | Q(email__icontains=busca))
    else:
        usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios, 'busca': busca})


def editar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    perfil, created = PerfilUsuario.objects.get_or_create(user=user)

    if request.method == 'POST':
        old_nome = user.first_name
        old_email = user.email
        old_tipo_tecnico = perfil.tipo_tecnico

        novo_nome = request.POST.get('nome')
        novo_email = request.POST.get('email')
        novo_tipo_tecnico = request.POST.get('tipo_tecnico')

        user.first_name = novo_nome
        user.email = novo_email
        user.save()

        perfil.tipo_tecnico = novo_tipo_tecnico
        perfil.save()

        mudanças = []
        if old_nome != novo_nome:
            mudanças.append(f"Nome: '{old_nome}' → '{novo_nome}'")
        if old_email != novo_email:
            mudanças.append(f"Email: '{old_email}' → '{novo_email}'")
        if old_tipo_tecnico != novo_tipo_tecnico:
            mudanças.append(
                f"Tipo Técnico: '{old_tipo_tecnico}' → '{novo_tipo_tecnico}'")

        if mudanças:
            messages.success(
                request, "Usuário atualizado com sucesso: " + ", ".join(mudanças))
        else:
            messages.info(request, "Nenhuma alteração feita.")

    return redirect('usuarios:lista_usuarios')


@require_POST
def excluir_usuario(request, user_id):
    if request.user.is_superuser:
        User.objects.filter(id=user_id).delete()
    return redirect('usuarios:lista_usuarios')

