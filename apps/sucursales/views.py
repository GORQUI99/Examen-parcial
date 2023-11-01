#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SucursalForm
from common.models import Sucursales
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import SucursalFilter

# Crear Sucursal
@login_required
def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_sucursales')
    else:
        form = SucursalForm()
    return render(request, 'sucursal/crear.html', {'form': form})


# Editar Sucursal
@login_required
def editar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursales, pk=id)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('listar_sucursales')
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'sucursal/editar.html', {'form': form, 'sucursal': sucursal})


# Eliminar Sucursal
@login_required
def eliminar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursales, pk=id)
    if request.method == 'GET':
        sucursal.delete()
        return redirect('listar_sucursales')


# Listar Sucursales
@login_required
def listar_sucursales(request):
    sucursales = Sucursales.objects.all()
    sucursal_filter = SucursalFilter(request.GET, queryset=sucursales)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(sucursal_filter.qs, 10)  # 10 sucursales por página
    sucursales_paginadas = paginator.get_page(page)

    return render(request, 'sucursal/listar.html', 
                  {
                    'sucursal_filter': sucursal_filter, 
                    'sucursales_paginadas': sucursales_paginadas
                   })