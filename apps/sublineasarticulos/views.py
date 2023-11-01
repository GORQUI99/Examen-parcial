from django.shortcuts import render, redirect, get_object_or_404
from .forms import SublineaForm
from common.models import SublineasArticulos
from django.core.paginator import Paginator
from .filters import SublineaFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Crear Sublínea de Artículos
@login_required
def crear_sublinea(request):
    if request.method == 'POST':
        print(request.POST)  # Verifica si los datos se están recibiendo correctamente
        form = SublineaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_sublineas')
    else:
        form = SublineaForm()
    return render(request, 'sublineas/crear.html', {'form': form})


# Editar Sublínea de Artículos
@login_required
def editar_sublinea(request, id):
    sublinea = get_object_or_404(SublineasArticulos, pk=id)
    if request.method == 'POST':
        form = SublineaForm(request.POST, instance=sublinea)
        if form.is_valid():
            form.save()
            return redirect('listar_sublineas')
    else:
        form = SublineaForm(instance=sublinea)
    return render(request, 'sublineas/editar.html', {'form': form, 'sublinea': sublinea})

# Eliminar Sublínea de Artículos
@login_required
def eliminar_sublinea(request, id):
    sublinea = get_object_or_404(SublineasArticulos, pk=id)
    if request.method == 'GET':
        sublinea.delete()
        return redirect('listar_sublineas')

# Listar Sublíneas de Artículos
@login_required
def listar_sublineas(request):
    sublineas = SublineasArticulos.objects.all()
    sublinea_filter = SublineaFilter(request.GET, queryset=sublineas)
    print(sublineas)
    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(sublinea_filter.qs, 10)  # 10 sublíneas por página
    sublineas_paginadas = paginator.get_page(page)

    return render(request, 'sublineas/listar.html', 
                  {
                    'sublinea_filter': sublinea_filter, 
                    'sublineas_paginadas': sublineas_paginadas
                   })
