
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    


    path("admin/", admin.site.urls),
    path("empresa/", include("apps.empresa.urls")),
    path("sucursales/", include("apps.sucursales.urls")),
    path("articulos/", include("apps.articulos.urls")),
    path("marcas/", include("apps.marcas.urls")),
    path("gruposproveedor/", include("apps.gruposproveedor.urls")),
    path("lineasarticulos/", include("apps.lineasarticulos.urls")),
    path("sublineasarticulos/", include("apps.sublineasarticulos.urls")),
    path("unidadesmedida/", include("apps.unidadesmedida.urls")),
    path("personal/", include("apps.personal.urls")),
    path("inventarios/", include("apps.inventarios.urls")),
    path("itemsinventario/", include("apps.itemsinventario.urls")),
    path("usuarios/", include("apps.usuarios.urls")),
    #auth
    path('', home_view, name='home'),
     path('accounts/login/', home_view, name='login_acounts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
