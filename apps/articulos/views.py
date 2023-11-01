#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticuloForm
from common.models import Articulos
from django.core.paginator import Paginator
from .filters import ArticuloFilter
from django.contrib.auth.decorators import login_required
# Crear Artículo
@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'articulos/crear.html', {'form': form})

# Editar Artículo
@login_required
def editar_articulo(request, id):
    articulo = get_object_or_404(Articulos, pk=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulos/editar.html', {'form': form, 'articulo': articulo})

# Eliminar Artículo
@login_required
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulos, pk=id)
    if request.method == 'GET':
        articulo.delete()
        return redirect('listar_articulos')

# Listar Artículos
@login_required
def listar_articulos(request):
    articulos = Articulos.objects.all()
    articulo_filter = ArticuloFilter(request.GET, queryset=articulos)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(articulo_filter.qs, 10)  # 10 artículos por página
    articulos_paginados = paginator.get_page(page)

    return render(request, 'articulos/listar.html', {'articulo_filter': articulo_filter, 'articulos_paginados': articulos_paginados})
