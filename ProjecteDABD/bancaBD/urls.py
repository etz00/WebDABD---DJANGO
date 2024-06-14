"""
URL configuration for bancaBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from bancaCatalana import views


urlpatterns = [
    path('', views.home, name='home'),  # Pàgina d'inici
    path("admin/", admin.site.urls),
    path('ciutats/', views.ciutats, name='ciutats'),
    path('ciutats/editar/<str:nom>/', views.editar_ciutat, name='editar_ciutat'),
    path('ciutats/eliminar/<str:nom>/', views.eliminar_ciutat, name='eliminar_ciutat'),
    path('oficines_centrals/', views.oficines_centrals, name='oficines_centrals'),
    path('oficines_centrals/editar/<str:id_oficina>/', views.editar_oficina, name='editar_oficina'),
    path('oficines_centrals/eliminar/<str:id_oficina>/', views.eliminar_oficina, name='eliminar_oficina'),
    path('gestors/', views.gestors, name='gestors'),
    path('sucursals/', views.sucursals, name='sucursals'),
    path('clients/', views.llista_clients, name='llista_clients'),
    path('particulars/', views.particulars, name='particulars'),
    path('empreses/', views.empreses, name='empreses'),
    path('comptes/', views.llista_comptes, name='llista_comptes'),
    path('operacions/', views.llista_operacions, name='llista_operacions'),
    path('transferencies/', views.transferencies, name='transferencies'),
]
