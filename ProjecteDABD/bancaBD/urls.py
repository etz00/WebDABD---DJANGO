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
    path('ciutats/afegir/', views.afegir_ciutat, name='afegir_ciutat'),
    path('ciutats/editar/<str:nom>/', views.editar_ciutat, name='editar_ciutat'),
    path('ciutats/eliminar/<str:nom>/', views.eliminar_ciutat, name='eliminar_ciutat'),
    path('oficines_centrals/', views.oficines_centrals, name='oficines_centrals'),
    path('oficines_centrals/nova/', views.afegir_oficina, name='afegir_oficina'),
    path('oficines_centrals/editar/<str:id_oficina>/', views.editar_oficina, name='editar_oficina'),
    path('oficines_centrals/eliminar/<str:id_oficina>/', views.eliminar_oficina, name='eliminar_oficina'),
    path('gestors/', views.gestors, name='gestors'),
    path('gestors/afegir/', views.afegir_gestor, name='afegir_gestor'),
    path('gestors/editar/<int:id_empleat>/', views.editar_gestor, name='editar_gestor'),
    path('gestors/eliminar/<int:id_empleat>/', views.eliminar_gestor, name='eliminar_gestor'),
    path('sucursals/', views.sucursals, name='sucursals'),
    path('sucursals/afegir/', views.afegir_sucursal, name='afegir_sucursal'),
    path('sucursals/editar/<int:id_sucursal>/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursals/eliminar/<int:id_sucursal>/', views.eliminar_sucursal, name='eliminar_sucursal'),
    path('clients/', views.llista_clients, name='llista_clients'),
    path('clients/afegir/', views.afegir_client, name='afegir_client'),
    path('clients/editar/<str:nif>/', views.editar_client, name='editar_client'),
    path('clients/eliminar/<str:nif>/', views.eliminar_client, name='eliminar_client'),
    path('particulars/', views.particulars, name='particulars'),
    path('particulars/afegir/', views.afegir_particular, name='afegir_particular'),
    path('particulars/editar/<str:nif>/', views.editar_particular, name='editar_particular'),
    path('particulars/eliminar/<str:nif>/', views.eliminar_particular, name='eliminar_particular'),
    path('empreses/', views.empreses, name='empreses'),
    path('empreses/afegir/', views.afegir_empresa, name='afegir_empresa'),
    path('empreses/editar/<str:nif>/', views.editar_empresa, name='editar_empresa'),
    path('empreses/eliminar/<str:nif>/', views.eliminar_empresa, name='eliminar_empresa'),
    path('comptes/', views.llista_comptes, name='llista_comptes'),
    path('comptes/afegir/', views.afegir_compte, name='afegir_compte'),
    path('comptes/editar/<str:iban>/', views.editar_compte, name='editar_compte'),
    path('comptes/eliminar/<str:iban>/', views.eliminar_compte, name='eliminar_compte'),
    path('operacions/', views.llista_operacions, name='llista_operacions'),
    path('operacions/afegir/', views.afegir_operacio, name='afegir_operacio'),
    path('operacions/editar/<int:id_operacio>/', views.editar_operacio, name='editar_operacio'),
    path('operacions/eliminar/<int:id_operacio>/', views.eliminar_operacio, name='eliminar_operacio'),
    path('transferencies/', views.transferencies, name='transferencies'),
    path('transferencies/afegir/', views.afegir_transferencia, name='afegir_transferencia'),
    path('transferencies/editar/<int:id_operacio>/', views.editar_transferencia, name='editar_transferencia'),
    path('transferencies/eliminar/<int:id_operacio>/', views.eliminar_transferencia, name='eliminar_transferencia'),
    path('buscar_nifs/', views.buscar_nifs, name='buscar_nifs'),
]
