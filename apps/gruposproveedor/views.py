from django.shortcuts import render, redirect, get_object_or_404
from .forms import GruposProveedorForm
from django.contrib.auth.decorators import login_required
from common.models import GruposProveedor
from django.core.paginator import Paginator
from .filters import GruposProveedorFilter
@login_required
def crear_grupo_proveedor(request):
    if request.method == 'POST':
        form = GruposProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos_proveedor')
    else:
        form = GruposProveedorForm()
    return render(request, 'grupos_proveedor/crear.html', {'form': form})
@login_required
def editar_grupo_proveedor(request, id):
    grupo = get_object_or_404(GruposProveedor, pk=id)
    if request.method == 'POST':
        form = GruposProveedorForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos_proveedor')
    else:
        form = GruposProveedorForm(instance=grupo)
    return render(request, 'grupos_proveedor/editar.html', {'form': form, 'grupo': grupo})
@login_required
def eliminar_grupo_proveedor(request, id):
    grupo = get_object_or_404(GruposProveedor, pk=id)
    if request.method == 'GET':
        grupo.delete()
        return redirect('listar_grupos_proveedor')
@login_required
def listar_grupos_proveedor(request):
    grupos = GruposProveedor.objects.all()
    grupo_filter = GruposProveedorFilter(request.GET, queryset=grupos)

    page = request.GET.get('page', 1)
    paginator = Paginator(grupo_filter.qs, 10)
    grupos_paginados = paginator.get_page(page)

    return render(request, 'grupos_proveedor/listar.html',
                  {
                    'grupo_filter': grupo_filter,
                    'grupos_paginados': grupos_paginados
                   })
