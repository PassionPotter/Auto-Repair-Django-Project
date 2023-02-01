"""SistemaCarros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Usuarios import views as user_views
from Usuarios.views import PasswordsChangeView, EditProfilePageView
from . import views as sistema_views, views
from django.contrib.auth import views as authentication_views, logout
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('carros/',include('carros.urls')),
    path('cliente-empresas/',include('ClienteEmpresas.urls')),
    path('clientes/', include('Clientes.urls')),
    #path('presupuestos/', include('Presupuestos.urls')),
    path('estimates/', include('Presupuestos.urls')),
    path('mano-obra/', include('ManoObra.urls')),
    path('parte/', include('Parte.urls')),
    path('informacion-tiendas/', include('InformacionTiendas.urls')),
    path('pagos/', include('Pagos.urls')),
    path('reports/', include('ReporteGanancias.urls')),
    path('foto/', include('Foto.urls')),
    path('detalle/', include('Detalle.urls')),
    path('invoices/', include('invoices.urls')),
    path('technicians/', include('tecnicos.urls')),
    # path('inventory/', include('inventory.urls')),
    #Dashboard
    #path('nuevo_cliente',user_views.nuevo_cliente, name='nuevo_cliente'),


    #Authentications
    path('registro/',user_views.registro,name='registro'),
    path('login/',authentication_views.LoginView.as_view(template_name='Usuarios/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='Usuarios/logout.html'),name='logout'),
    path('profile/',user_views.profilepage,name='profile'),
    path('profile/change-password/',PasswordsChangeView.as_view(template_name='Usuarios/change-password.html'),name='change-password'),
    path('password_success',user_views.password_success,name="password_success"),
    path('profile/<int:pk>/edit-profile/',EditProfilePageView.as_view(),name='edit-profile'),

    #RichFields
    path('djrichtextfield/', include('djrichtextfield.urls')),

    #search
    path('search/',sistema_views.search, name='search'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        ) 
