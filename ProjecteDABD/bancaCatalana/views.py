from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Ciutat, OficinaCentral, Gestor, Sucursal, Client, Particular, Empresa, Compte, Operacio, Efectiu, Transferencia, CarrecComissions


def home(request):
    return render(request, 'home.html')

def ciutats(request):
    query = request.GET.get('search', '')
    if query:
        ciutats_list = Ciutat.objects.filter(nom__icontains=query)
    else:
        ciutats_list = Ciutat.objects.all()
    
    paginator = Paginator(ciutats_list, 25)  # Mostra 25 ciutats per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ciutats.html', {'page_obj': page_obj})

def editar_ciutat(request, nom):
    ciutat = get_object_or_404(Ciutat, nom=nom)    
    if request.method == 'POST':
        nou_nom = request.POST.get('nom')
        if nou_nom and nou_nom != nom:
            if Ciutat.objects.filter(nom=nou_nom).exists():
                messages.error(request, "El nom de la ciutat ja existeix.")
            else:
                Ciutat.objects.filter(nom=nom).update(nom=nou_nom)
                messages.success(request, "Ciutat modificada correctament.")
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

def afegir_ciutat(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        if nom:
            if Ciutat.objects.filter(nom=nom).exists():
                messages.error(request, "La ciutat ja existeix.")
            else:
                Ciutat.objects.create(nom=nom)
                messages.success(request, "Ciutat afegida correctament.")
                return redirect('ciutats')
    return render(request, 'afegir_ciutat.html')

def oficines_centrals(request):
    query = request.GET.get('search', '')
    if query:
        oficines_list = OficinaCentral.objects.filter(nom_ciutat__nom__icontains=query)
    else:
        oficines_list = OficinaCentral.objects.all()
    
    paginator = Paginator(oficines_list, 25)  # Mostra 25 oficines per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'oficines_centrals.html', {'page_obj': page_obj})

def editar_oficina(request, id_oficina):
    oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
    if request.method == 'POST':
        nou_id_oficina = request.POST.get('id_oficina')
        nous_empleats = request.POST.get('empleats')
        nom_ciutat = request.POST.get('nom_ciutat')

        # Asegurar que los inputs no son vacíos
        if nou_id_oficina and nous_empleats and nom_ciutat:
            if OficinaCentral.objects.filter(id_oficina=nou_id_oficina).exclude(id_oficina=oficina.id_oficina).exists():
                messages.error(request, "El ID de l'oficina ja existeix.")
            else:
                try:
                    ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
                    oficina.id_oficina = nou_id_oficina
                    oficina.empleats = nous_empleats
                    oficina.nom_ciutat = ciutat
                    oficina.save()
                    messages.success(request, "Oficina Central actualitzada correctament.")
                    return redirect('oficines_centrals')
                except Ciutat.DoesNotExist:
                    messages.error(request, "La ciutat proporcionada no existeix.")
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

def nova_oficina(request):
    if request.method == 'POST':
        id_oficina = request.POST.get('id_oficina')
        empleats = request.POST.get('empleats')
        nom_ciutat = request.POST.get('nom_ciutat')

        if id_oficina and empleats and nom_ciutat:
            if OficinaCentral.objects.filter(id_oficina=id_oficina).exists():
                messages.error(request, "El ID de l'oficina ja existeix.")
            else:
                ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
                OficinaCentral.objects.create(id_oficina=id_oficina, empleats=empleats, nom_ciutat=ciutat)
                messages.success(request, "Oficina Central creada correctament.")
                return redirect('oficines_centrals')
    return render(request, 'nova_oficina.html')



def gestors(request):
    query = request.GET.get('search', '')
    if query:
        gestors_list = Gestor.objects.filter(nom__icontains=query)
    else:
        gestors_list = Gestor.objects.all()
    
    paginator = Paginator(gestors_list, 25)  # Mostra 25 gestors per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gestors.html', {'page_obj': page_obj})



def afegir_gestor(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        data_inici = request.POST.get('data_inici')
        if nom and data_inici:
            Gestor.objects.create(nom=nom, data_inici=data_inici)
            messages.success(request, "Gestor afegit correctament.")
            return redirect('gestors')
    return render(request, 'afegir_gestor.html')


def editar_gestor(request, id_empleat):
    gestor = get_object_or_404(Gestor, id_empleat=id_empleat)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        data_inici = request.POST.get('data_inici')
        if nom and data_inici:
            gestor.nom = nom
            gestor.data_inici = data_inici
            gestor.save()
            messages.success(request, "Gestor actualitzat correctament.")
            return redirect('gestors')
    return render(request, 'editar_gestor.html', {'gestor': gestor})


def eliminar_gestor(request, id_empleat):
    gestor = get_object_or_404(Gestor, id_empleat=id_empleat)
    if request.method == 'POST':
        try:
            gestor.delete()
            messages.success(request, "Gestor eliminat correctament.")
        except ProtectedError:
            messages.error(request, "No es pot eliminar el gestor perquè té associacions.")
        return redirect('gestors')
    return render(request, 'gestors.html', {'gestors': Gestor.objects.all()})


def sucursals(request):
    sucursals_list = Sucursal.objects.all()
    paginator = Paginator(sucursals_list, 25)  # Mostra 25 sucursals per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sucursals.html', {'page_obj': page_obj})


def llista_clients(request):
    clients_list = Client.objects.all()
    paginator = Paginator(clients_list, 25)  # Mostra 25 clients per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'clients.html', {'page_obj': page_obj})


def particulars(request):
    particulars_list = Particular.objects.all()
    paginator = Paginator(particulars_list, 25)  # Mostra 25 particulars per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'particulars.html', {'page_obj': page_obj})


def empreses(request):
    empreses_list = Empresa.objects.all()
    paginator = Paginator(empreses_list, 25)  # Mostra 25 empreses per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'empreses.html', {'page_obj': page_obj})


def llista_comptes(request):
    comptes_list = Compte.objects.all()
    paginator = Paginator(comptes_list, 25)  # Mostra 25 comptes per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'comptes.html', {'page_obj': page_obj})


def llista_operacions(request):
    operacions_list = Operacio.objects.all()
    paginator = Paginator(operacions_list, 25)  # Mostra 25 operacions per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'operacions.html', {'page_obj': page_obj})


def transferencies(request):
    transferencies_list = Transferencia.objects.all()
    paginator = Paginator(transferencies_list, 25)  # Mostra 25 transferències per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'transferencies.html', {'page_obj': page_obj})
