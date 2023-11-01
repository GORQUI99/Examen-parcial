# En views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MarcaForm
from common.models import Marcas
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import MarcaFilter

# Crear Marca
@login_required
def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm()
    return render(request, 'marcas/crear.html', {'form': form})

# Editar Marca
@login_required
def editar_marca(request, id):
    marca = get_object_or_404(Marcas, pk=id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'marcas/editar.html', {'form': form, 'marca': marca})

# Eliminar Marca
@login_required
def eliminar_marca(request, id):
    marca = get_object_or_404(Marcas, pk=id)
    if request.method == 'GET':
        marca.delete()
        return redirect('listar_marcas')

# Listar Marcas
@login_required
def listar_marcas(request):
    marcas = Marcas.objects.all()
    marca_filter = MarcaFilter(request.GET, queryset=marcas)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(marca_filter.qs, 10)  # 10 marcas por página
    marcas_paginadas = paginator.get_page(page)

    return render(request, 'marcas/listar.html', 
                  {
                    'marca_filter': marca_filter, 
                    'marcas_paginadas': marcas_paginadas
                   })