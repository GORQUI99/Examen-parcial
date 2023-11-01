from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import uuid


class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nro_documento = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Razón Social: {self.razon_social}, Número de Documento: {self.nro_documento}'

class Sucursales(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre_comercial = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Nombre Comercial: {self.nombre_comercial}, Empresa: {self.empresa.razon_social}'


class Marcas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_marca = models.CharField(max_length=8, unique=True, editable=False)
    marca_nombre = models.CharField(max_length=150)
    
    @staticmethod
    def generate_codigo():
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.codigo_marca:
            self.codigo_marca = self.generate_codigo()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Marca: {self.marca_nombre}'
    
class GruposProveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_grupo = models.CharField(max_length=8, unique=True, editable=False)
    grupo_descripcion = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_grupo = models.CharField(max_length=25)
    @staticmethod
    def generate_codigo():
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.codigo_grupo:
            self.codigo_grupo = self.generate_codigo()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Descripción Grupo: {self.grupo_descripcion}, Empresa: {self.empresa.razon_social}'

class LineasArticulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_linea = models.CharField(max_length=8, unique=True, editable=False)
    linea_descripcion = models.CharField(max_length=100)
    grupo = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_linea = models.CharField(max_length=25)
    @staticmethod
    def generate_codigo():
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.codigo_linea:
            self.codigo_linea = self.generate_codigo()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Línea Descripción: {self.linea_descripcion}, Grupo: {self.grupo.grupo_descripcion}'

class SublineasArticulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_sublinea = models.CharField(max_length=8, unique=True, editable=False)
    sublinea_descripcion = models.CharField(max_length=100)
    linea = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    estado = models.BooleanField()
    @staticmethod
    def generate_codigo():
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.codigo_sublinea:
            self.codigo_sublinea = self.generate_codigo()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Sublínea Descripción: {self.sublinea_descripcion}, Línea: {self.linea.linea_descripcion}'

    
class UnidadesMedida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unidad_nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Unidad de Medida: {self.unidad_nombre}'


class Articulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_sku = models.CharField(max_length=8, unique=True, editable=False)
    descripcion = models.CharField(max_length=150)
    unidad_medida = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE)
    linea = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    sublinea = models.ForeignKey(SublineasArticulos, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    factor_compra = models.IntegerField()
    factor_reparto = models.IntegerField()
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    @staticmethod
    def generate_codigo():
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.codigo_sku:
            self.codigo_sku = self.generate_codigo()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Descripción Artículo: {self.descripcion}, Empresa: {self.empresa.razon_social}'




class Personal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_personal = models.CharField(max_length=100)
    direccion_personal = models.CharField(max_length=150)
    TIPO = (
        ('DNI', 'Documento N. Identidad'),
        ('CNT', 'Carnet de Extranjeria'),
    )
    tipo_documento = models.CharField(max_length=3, choices=TIPO, default='DNI')
    nro_documento = models.CharField(max_length=11)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Añadí la relación con Empresa
    
    def __str__(self):
        return f'Nombre Personal: {self.nombre_personal}, Empresa: {self.empresa.razon_social}'


class Inventarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha_inventario = models.DateTimeField()
    nro_inventario = models.IntegerField()
    responsable = models.ForeignKey(Personal, on_delete=models.CASCADE)  # Añadí la relación con Personal
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    total_inventario = models.DecimalField(max_digits=12, decimal_places=2)
    ESTADOS = (
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Closed'),
    )
    estado = models.CharField(max_length=2, choices=ESTADOS, default='P')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventarios_registrados')
    cerrado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventarios_cerrados', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Nro Inventario: {self.nro_inventario}, Empresa: {self.empresa.razon_social}, Sucursal: {self.sucursal.nombre_comercial}'




class ItemsInventario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventario = models.ForeignKey(Inventarios, on_delete=models.CASCADE)
    nro_item = models.IntegerField()
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    stock_fisico = models.DecimalField(max_digits=12, decimal_places=2)
    devoluciones_pendientes = models.DecimalField(max_digits=12, decimal_places=2)
    total_unidades_stock = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)
    def save(self, *args, **kwargs):
            # c) No se pueden registrar dos mismos articulos para un inventario
            if ItemsInventario.objects.filter(inventario=self.inventario, articulo=self.articulo).exists():
                raise ValidationError("Este artículo ya ha sido registrado en este inventario.")

            super(ItemsInventario, self).save(*args, **kwargs)    
    def __str__(self):
        return f'Nro Item: {self.nro_item}, Inventario: {self.inventario.nro_inventario}, Artículo: {self.articulo.descripcion}'




