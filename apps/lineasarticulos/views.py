# En views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LineasArticulosForm
from django.contrib.auth.decorators import login_required
from common.models import LineasArticulos
from django.core.paginator import Paginator
from .filters import LineasArticulosFilter

# Crear Línea de Artículos
@login_required
def crear_linea_articulos(request):
    if request.method == 'POST':
        form = LineasArticulosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_lineas_articulos')
    else:
        form = LineasArticulosForm()
    return render(request, 'lineas_articulos/crear.html', {'form': form})

# Editar Línea de Artículos
@login_required
def editar_linea_articulos(request, id):
    linea_articulo = get_object_or_404(LineasArticulos, pk=id)
    if request.method == 'POST':
        form = LineasArticulosForm(request.POST, instance=linea_articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_lineas_articulos')
    else:
        form = LineasArticulosForm(instance=linea_articulo)
    return render(request, 'lineas_articulos/editar.html', {'form': form, 'linea_articulo': linea_articulo})

# Eliminar Línea de Artículos
@login_required
def eliminar_linea_articulos(request, id):
    linea_articulo = get_object_or_404(LineasArticulos, pk=id)
    if request.method == 'GET':
        linea_articulo.delete()
        return redirect('listar_lineas_articulos')

# Listar Líneas de Artículos
@login_required
def listar_lineas_articulos(request):
    lineas_articulos = LineasArticulos.objects.all()
    linea_articulo_filter = LineasArticulosFilter(request.GET, queryset=lineas_articulos)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(linea_articulo_filter.qs, 10)  # 10 líneas de artículos por página
    lineas_articulos_paginadas = paginator.get_page(page)

    return render(request, 'lineas_articulos/listar.html', 
                  {
                    'linea_articulo_filter': linea_articulo_filter, 
                    'lineas_articulos_paginadas': lineas_articulos_paginadas
                   })
