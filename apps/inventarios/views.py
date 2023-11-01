from django.shortcuts import render, redirect, get_object_or_404
from common.models import Inventarios
from .forms import InventariosForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import InventariosFilter
@login_required
def listar_inventarios(request):
    inventarios = Inventarios.objects.all()
    inventarios_filter = InventariosFilter(request.GET, queryset=inventarios)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(inventarios_filter.qs, 10)  # 10 inventarios por página
    inventarios_paginados = paginator.get_page(page)

    return render(request, 'inventarios/listar.html',
                  {
                      'inventarios_filter': inventarios_filter,
                      'inventarios_paginados': inventarios_paginados
                   })
@login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inventarios')
    else:
        form = InventariosForm()
    return render(request, 'inventarios/crear.html', {'form': form})
@login_required
def editar_inventario(request, id):
    inventario = get_object_or_404(Inventarios, pk=id)
    if request.method == 'POST':
        form = InventariosForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('listar_inventarios')
    else:
        form = InventariosForm(instance=inventario)
    return render(request, 'inventarios/editar.html', {'form': form, 'inventario': inventario})
@login_required
def eliminar_inventario(request, id):
    inventario = get_object_or_404(Inventarios, pk=id)
    if request.method == 'GET':
        inventario.delete()
        return redirect('listar_inventarios')
