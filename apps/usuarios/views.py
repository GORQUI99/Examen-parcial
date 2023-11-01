from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def crear_usuario(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Cifra la contraseña
            user.save()
            return redirect('login')  # Cambia esto a tu ruta deseada
    else:
        form = RegisterForm()
    return render(request, 'usuarios/register.html', {'form': form})



@csrf_protect
def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        else:
            messages.error(request, 'El formulario no es válido. Por favor, verifica los campos.')

    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
