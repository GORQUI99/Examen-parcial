# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UnidadMedidaForm
from common.models import UnidadesMedida
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import UnidadMedidaFilter

# Crear Unidad de Medida
@login_required
def crear_unidad_medida(request):
    if request.method == 'POST':
        form = UnidadMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades_medida')
    else:
        form = UnidadMedidaForm()
    return render(request, 'unidades_medida/crear.html', {'form': form})

# Editar Unidad de Medida
@login_required
def editar_unidad_medida(request, id):
    unidad_medida = get_object_or_404(UnidadesMedida, id=id)
    if request.method == 'POST':
        form = UnidadMedidaForm(request.POST, instance=unidad_medida)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades_medida')
    else:
        form = UnidadMedidaForm(instance=unidad_medida)
    return render(request, 'unidades_medida/editar.html', {'form': form, 'unidad_medida': unidad_medida})

# Eliminar Unidad de Medida
@login_required
def eliminar_unidad_medida(request, id):
    unidad_medida = get_object_or_404(UnidadesMedida, id=id)
    if request.method == 'GET':
        unidad_medida.delete()
        return redirect('listar_unidades_medida')

# Listar Unidades de Medida
@login_required
def listar_unidades_medida(request):
    unidades_medida = UnidadesMedida.objects.all()
    unidad_medida_filter = UnidadMedidaFilter(request.GET, queryset=unidades_medida)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(unidad_medida_filter.qs, 10)  # 10 unidades de medida por página
    unidades_medida_paginadas = paginator.get_page(page)

    return render(request, 'unidades_medida/listar.html', 
                  {
                    'unidad_medida_filter': unidad_medida_filter, 
                    'unidades_medida_paginadas': unidades_medida_paginadas
                   })
