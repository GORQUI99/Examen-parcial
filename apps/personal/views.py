from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonalForm
from django.contrib.auth.decorators import login_required
from common.models import Personal
from django.core.paginator import Paginator
from .filters import PersonalFilter

# Crear Personal
@login_required
def crear_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personal')
    else:
        form = PersonalForm()
    return render(request, 'personal/crear.html', {'form': form})

# Editar Personal
@login_required
def editar_personal(request, id):
    personal = get_object_or_404(Personal, pk=id)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('listar_personal')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'personal/editar.html', {'form': form, 'personal': personal})

# Eliminar Personal
@login_required
def eliminar_personal(request, id):
    personal = get_object_or_404(Personal, pk=id)
    if request.method == 'GET':
        personal.delete()
        return redirect('listar_personal')

# Listar Personal
@login_required
def listar_personal(request):
    personal = Personal.objects.all()
    personal_filter = PersonalFilter(request.GET, queryset=personal)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(personal_filter.qs, 10)  # 10 elementos por página
    personal_paginado = paginator.get_page(page)

    return render(request, 'personal/listar.html', 
                  {
                    'personal_filter': personal_filter, 
                    'personal_paginado': personal_paginado
                   })
