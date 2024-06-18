from pyexpat.errors import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Ciutat, OficinaCentral, Gestor, Sucursal, Client, Particular, Empresa, Compte, Operacio, Efectiu, Transferencia, CarrecComissions, RelacioTransferencies


def home(request):
    return render(request, 'home.html')


def ciutats(request):
    query = request.GET.get('search', '')
    if query:
        ciutats = Ciutat.objects.filter(nom__icontains=query)
    else:
        ciutats = Ciutat.objects.all()
    
    return render(request, 'ciutats.html', {'ciutats': ciutats})


def editar_ciutat(request, nom):
    ciutat = get_object_or_404(Ciutat, nom=nom)    
    if request.method == 'POST':
        nou_nom = request.POST.get('nom')
        #nom_ciutat = request.POST.get('nom_ciutat')

        # Assegurar que els inputs no són buits
        if nou_nom:
            #nova_ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
            ciutat.nom = nou_nom
            ciutat.save()
            return redirect('ciutats')
    return render(request, 'editar_ciutat.html', {'ciutat': ciutat})


def eliminar_ciutat(request, nom):
    ciutat = get_object_or_404(Ciutat, nom=nom)
    if request.method == 'POST':
        try:
            ciutat.delete()
            messages.success(request, "Ciutat eliminada correctament.")
        except ProtectedError:
            messages.error(request, "No es pot eliminar la ciutat perquè té oficines centrals associades.")

        return redirect('ciutats')

    return render(request, 'ciutats.html', {'ciutats': Ciutat.objects.all()})


#def oficines_centrals(request):
    oficines = OficinaCentral.objects.all()
    #for oficina in oficines:
    #    print(oficina.nom)
    return render(request, 'oficines_centrals.html', {'oficines': oficines})

def oficines_centrals(request):
    query = request.GET.get('search', '')
    if query:
        oficines = OficinaCentral.objects.filter(nom_ciutat__nom__icontains=query)
    else:
        oficines = OficinaCentral.objects.all()

    return render(request, 'oficines_centrals.html', {'oficines': oficines})

def editar_oficina(request, id_oficina):
    oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
    if request.method == 'POST':
        nou_id_oficina = request.POST.get('id_oficina')
        nous_empleats = request.POST.get('empleats')
        nom_ciutat = request.POST.get('nom_ciutat')

        # Assegurar que els inputs no són buits
        if nou_id_oficina and nous_empleats and nom_ciutat:
            nova_ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
            oficina.id_oficina = nou_id_oficina
            oficina.empleats = nous_empleats
            oficina.nom_ciutat = nova_ciutat
            oficina.save()
            return redirect('oficines_centrals')
    return render(request, 'editar_oficina.html', {'oficina': oficina})

def eliminar_oficina(request, id_oficina):
    oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)

    if request.method == 'POST':
        try:
            oficina.delete()
            messages.success(request, "Oficina Central eliminada correctament.")
        except ProtectedError:
            messages.error(request, "No es pot eliminar l'Oficina Central perquè té sucursals associades.")

        return redirect('oficines_centrals')

    return render(request, 'oficines_centrals.html', {'oficines': OficinaCentral.objects.all()})

def gestors(request):
    gestors = Gestor.objects.all()
    for gestor in gestors:
        print(gestor.nom)
    return render(request, 'gestors.html', {'gestors': gestors})


def sucursals(request):
    sucursals = Sucursal.objects.all()
    for sucursal in sucursals:
        if sucursal.nom_ciutat is not None:
            print(sucursal.nom_ciutat.nom)
        else:
            print("No té ciutat assignada")
    return render(request, 'sucursals.html', {'sucursals': sucursals})


def llista_clients(request):
    clients_list = Client.objects.all()
    paginator = Paginator(clients_list, 20)  # Mostra 20 clients per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print(page_obj.object_list)  # Línia de depuració
    
    return render(request, 'clients.html', {'page_obj': page_obj})


def particulars(request):
    particulars = Particular.objects.all()
    for particular in particulars:
        print(particular.nif)
    return render(request, 'particulars.html', {'particulars': particulars})


def empreses(request):
    empreses_list = Empresa.objects.all()
    print(empreses_list)  # Línea de depuración
    paginator = Paginator(empreses_list, 20)  # Mostra 20 empreses per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print(page_obj.object_list)  # Línia de depuració
    
    return render(request, 'empreses.html', {'page_obj': page_obj})



def llista_comptes(request):
    comptes_list = Compte.objects.all()
    paginator = Paginator(comptes_list, 20)  # Mostra 10 clients per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print(page_obj.object_list)  # Línia de depuració
    
    return render(request, 'comptes.html', {'page_obj': page_obj})

def llista_operacions(request):
    operacions_list = Operacio.objects.all()
    paginator = Paginator(operacions_list, 20)  # Mostra 10 clients per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    print(page_obj.object_list)  # Línia de depuració
    
    return render(request, 'operacions.html', {'page_obj': page_obj})


def transferencies(request):
    transferencies_list = Transferencia.objects.all()
    paginator = Paginator(transferencies_list, 20)  # Mostrará 20 transferencias por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'transferencies.html', {'page_obj': page_obj})



