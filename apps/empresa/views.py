from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EmpresaForm
from common.models import Empresa
from django.core.paginator import Paginator
from common.models import Empresa
from .filters import EmpresaFilter
@login_required
def crear_empresa(request):
    """
    VISTA CON FORMULARIO DE NUEVA EMPRESA 
    """
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empresas')  # Redirige a la lista de empresas
    else:
        form = EmpresaForm()
    return render(request, 'empresa/crear.html', {'form': form})

@login_required
def editar_empresa(request, id):
    """
    VISTA CON FORMULARIO DE EDITAR EMPRESA 
    """
    empresa = get_object_or_404(Empresa, pk=id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('listar_empresas')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa/editar.html', {'form': form, 'empresa': empresa})
@login_required
def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.method == 'GET':
        empresa.delete()
        return redirect('listar_empresas')
   
@login_required
def listar_empresas(request):
    empresas = Empresa.objects.all()
    empresa_filter = EmpresaFilter(request.GET, queryset=empresas)

    # Agrega paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(empresa_filter.qs, 10)  # 10 empresas por página
    empresas_paginadas = paginator.get_page(page)

    return render(request, 'empresa/listar.html', 
                  {
                    'empresa_filter': empresa_filter, 
                    'empresas_paginadas': empresas_paginadas
                   })