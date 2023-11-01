from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemsInventarioForm
from common.models import ItemsInventario
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import ItemsInventarioFilter
@login_required
def crear_items_inventario(request):
    if request.method == 'POST':
        form = ItemsInventarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_items_inventario')
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = ItemsInventarioForm()
    return render(request, 'items_inventario/crear.html', {'form': form})
@login_required
def listar_items_inventario(request):
    items_inventario = ItemsInventario.objects.all()
    items_inventario_filter = ItemsInventarioFilter(request.GET, queryset=items_inventario)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(items_inventario_filter.qs, 10)  # 10 items por página
    items_paginados = paginator.get_page(page)

    return render(request, 'items_inventario/listar.html', 
                  {'items_inventario_filter': items_inventario_filter, 'items_paginados': items_paginados})

@login_required
def editar_items_inventario(request, id):
    item = get_object_or_404(ItemsInventario, id=id)

    if request.method == 'POST':
        form = ItemsInventarioForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_items_inventario')
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = ItemsInventarioForm(instance=item)

    return render(request, 'items_inventario/editar.html', {'form': form, 'item': item})
@login_required
def eliminar_items_inventario(request, id):
    item = get_object_or_404(ItemsInventario, id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('listar_items_inventario')

    return render(request, 'items_inventario/confirmar_eliminar.html', {'item': item})
