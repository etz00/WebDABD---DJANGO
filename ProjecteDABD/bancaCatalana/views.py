from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.http import JsonResponse
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
    
    paginator = Paginator(oficines_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'oficines_centrals.html', {'page_obj': page_obj})

def afegir_oficina(request):
    if request.method == 'POST':
        id_oficina = request.POST.get('id_oficina')
        empleats = request.POST.get('empleats')
        nom_ciutat = request.POST.get('nom_ciutat')

        ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)

        OficinaCentral.objects.create(id_oficina=id_oficina, empleats=empleats, nom_ciutat=ciutat)
        messages.success(request, "Oficina central afegida correctament.")
        return redirect('oficines_centrals')
    
    ciutats = Ciutat.objects.all()
    return render(request, 'afegir_oficina.html', {'ciutats': ciutats})


def editar_oficina(request, id_oficina):
    oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
    if request.method == 'POST':
        nou_id_oficina = request.POST.get('id_oficina')
        nous_empleats = request.POST.get('empleats')
        nom_ciutat = request.POST.get('nom_ciutat')

        if nou_id_oficina:
            oficina.id_oficina = nou_id_oficina
        if nous_empleats:
            oficina.empleats = nous_empleats
        if nom_ciutat:
            oficina.nom_ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
        
        oficina.save()
        messages.success(request, "Oficina central modificada correctament.")
        return redirect('oficines_centrals')
    
    ciutats = Ciutat.objects.all()
    return render(request, 'editar_oficina.html', {'oficina': oficina, 'ciutats': ciutats})

def eliminar_oficina(request, id_oficina):
    oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
    if request.method == 'POST':
        oficina.delete()
        messages.success(request, "Oficina central eliminada correctament.")
        return redirect('oficines_centrals')
    return render(request, 'oficines_centrals.html', {'oficines': OficinaCentral.objects.all()})



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
    query = request.GET.get('search', '')
    if query:
        sucursals_list = Sucursal.objects.filter(id_sucursal__icontains=query)
    else:
        sucursals_list = Sucursal.objects.all()
    
    paginator = Paginator(sucursals_list, 25)  # Mostra 25 sucursals per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'sucursals.html', {'page_obj': page_obj})

def afegir_sucursal(request):
    if request.method == 'POST':
        carrer = request.POST.get('carrer')
        nom_ciutat = request.POST.get('nom_ciutat')
        id_oficina = request.POST.get('id_oficina')
        id_empleat = request.POST.get('id_empleat')

        ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
        oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
        empleat = get_object_or_404(Gestor, id_empleat=id_empleat)

        Sucursal.objects.create(carrer=carrer, nom_ciutat=ciutat, id_oficina=oficina, id_empleat=empleat)
        messages.success(request, "Sucursal afegida correctament.")
        return redirect('sucursals')
    
    ciutats = Ciutat.objects.all()
    oficines = OficinaCentral.objects.all()
    gestors = Gestor.objects.all()
    return render(request, 'afegir_sucursal.html', {'ciutats': ciutats, 'oficines': oficines, 'gestors': gestors})

def editar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        carrer = request.POST.get('carrer')
        nom_ciutat = request.POST.get('nom_ciutat')
        id_oficina = request.POST.get('id_oficina')
        id_empleat = request.POST.get('id_empleat')

        if carrer:
            sucursal.carrer = carrer
        if nom_ciutat:
            sucursal.nom_ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
        if id_oficina:
            sucursal.id_oficina = get_object_or_404(OficinaCentral, id_oficina=id_oficina)
        if id_empleat:
            sucursal.id_empleat = get_object_or_404(Gestor, id_empleat=id_empleat)
        
        sucursal.save()
        messages.success(request, "Sucursal modificada correctament.")
        return redirect('sucursals')
    
    ciutats = Ciutat.objects.all()
    oficines = OficinaCentral.objects.all()
    gestors = Gestor.objects.all()
    return render(request, 'editar_sucursal.html', {'sucursal': sucursal, 'ciutats': ciutats, 'oficines': oficines, 'gestors': gestors})

def eliminar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        sucursal.delete()
        messages.success(request, "Sucursal eliminada correctament.")
        return redirect('sucursals')
    return render(request, 'sucursals.html', {'sucursals': Sucursal.objects.all()})

def llista_clients(request):
    query = request.GET.get('search', '')
    if query:
        clients_list = Client.objects.filter(nif__icontains=query)
    else:
        clients_list = Client.objects.all()
    
    paginator = Paginator(clients_list, 25)  # Mostra 25 clients per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'clients.html', {'page_obj': page_obj})

def afegir_client(request):
    if request.method == 'POST':
        nif = request.POST.get('nif')
        nom = request.POST.get('nom')
        telefon = request.POST.get('telefon')
        adreca = request.POST.get('adreca')
        id_sucursal = request.POST.get('id_sucursal')
        
        if Client.objects.filter(nif=nif).exists():
            messages.error(request, "El NIF del client ja existeix.")
        else:
            sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
            Client.objects.create(nif=nif, nom=nom, telefon=telefon, adreca=adreca, id_sucursal=sucursal)
            messages.success(request, "Client afegit correctament.")
            return redirect('llista_clients')
    
    sucursals = Sucursal.objects.all()
    return render(request, 'afegir_client.html', {'sucursals': sucursals})

def editar_client(request, nif):
    client = get_object_or_404(Client, nif=nif)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        telefon = request.POST.get('telefon')
        adreca = request.POST.get('adreca')
        id_sucursal = request.POST.get('id_sucursal')
        
        if nom:
            client.nom = nom
        if telefon:
            client.telefon = telefon
        if adreca:
            client.adreca = adreca
        if id_sucursal:
            sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
            client.id_sucursal = sucursal
        
        client.save()
        messages.success(request, "Client modificat correctament.")
        return redirect('llista_clients')
    
    sucursals = Sucursal.objects.all()
    return render(request, 'editar_client.html', {'client': client, 'sucursals': sucursals})

def eliminar_client(request, nif):
    client = get_object_or_404(Client, nif=nif)
    if request.method == 'POST':
        client.delete()
        messages.success(request, "Client eliminat correctament.")
        return redirect('llista_clients')
    return render(request, 'llista_clients')


def particulars(request):
    query = request.GET.get('search', '')
    if query:
        particulars_list = Particular.objects.filter(nif__nif__icontains=query)
    else:
        particulars_list = Particular.objects.all()
    
    paginator = Paginator(particulars_list, 25)  # Mostra 25 particulars per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'particulars.html', {'page_obj': page_obj})

def afegir_particular(request):
    if request.method == 'POST':
        nif = request.POST.get('nif')
        ingressos_anuals = request.POST.get('ingressos_anuals')
        if nif and ingressos_anuals:
            client = get_object_or_404(Client, nif=nif)
            if Particular.objects.filter(nif=client).exists():
                messages.error(request, "Aquest NIF ja està registrat com a particular.")
            else:
                Particular.objects.create(nif=client, ingressos_anuals=ingressos_anuals)
                messages.success(request, "Particular afegit correctament.")
                return redirect('particulars')
    clients = Client.objects.exclude(nif__in=Particular.objects.values('nif')).exclude(nif__in=Empresa.objects.values('nif'))[:200]  # Limitar a 200 NIFs
    return render(request, 'afegir_particular.html', {'clients': clients})

def editar_particular(request, nif):
    particular = get_object_or_404(Particular, nif=nif)
    if request.method == 'POST':
        ingressos_anuals = request.POST.get('ingressos_anuals')
        particular.ingressos_anuals = ingressos_anuals
        particular.save()
        messages.success(request, "Particular modificat correctament.")
        return redirect('particulars')
    return render(request, 'editar_particular.html', {'particular': particular})

def eliminar_particular(request, nif):
    particular = get_object_or_404(Particular, nif=nif)
    if request.method == 'POST':
        particular.delete()
        messages.success(request, "Particular eliminat correctament.")
        return redirect('particulars')
    return render(request, 'particulars.html', {'page_obj': Particular.objects.all()})

def empreses(request):
    query = request.GET.get('search', '')
    if query:
        empreses_list = Empresa.objects.filter(nif__nif__icontains=query)
    else:
        empreses_list = Empresa.objects.all()
    
    paginator = Paginator(empreses_list, 25)  # Mostra 25 empreses per pàgina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'empreses.html', {'page_obj': page_obj})

def afegir_empresa(request):
    if request.method == 'POST':
        nif = request.POST.get('nif')
        facturacio = request.POST.get('facturacio')
        if nif and facturacio:
            client = get_object_or_404(Client, nif=nif)
            if Empresa.objects.filter(nif=client).exists():
                messages.error(request, "Aquest NIF ja està registrat com a empresa.")
            else:
                Empresa.objects.create(nif=client, facturacio=facturacio)
                messages.success(request, "Empresa afegida correctament.")
                return redirect('empreses')
    clients = Client.objects.exclude(nif__in=Particular.objects.values('nif')).exclude(nif__in=Empresa.objects.values('nif'))[:200]  # Limitar a 200 NIFs
    return render(request, 'afegir_empresa.html', {'clients': clients})

def editar_empresa(request, nif):
    empresa = get_object_or_404(Empresa, nif=nif)
    if request.method == 'POST':
        facturacio = request.POST.get('facturacio')
        empresa.facturacio = facturacio
        empresa.save()
        messages.success(request, "Empresa modificada correctament.")
        return redirect('empreses')
    return render(request, 'editar_empresa.html', {'empresa': empresa})

def eliminar_empresa(request, nif):
    empresa = get_object_or_404(Empresa, nif=nif)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, "Empresa eliminada correctament.")
        return redirect('empreses')
    return render(request, 'empreses.html', {'empreses': Empresa.objects.all()})


def llista_comptes(request):
    query = request.GET.get('search', '')
    if query:
        comptes_list = Compte.objects.filter(iban__icontains=query) | Compte.objects.filter(nif__nif__icontains=query)
    else:
        comptes_list = Compte.objects.all()
    
    paginator = Paginator(comptes_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'comptes.html', {'page_obj': page_obj})

def afegir_compte(request):
    if request.method == 'POST':
        iban = request.POST.get('iban')
        data_obertura = request.POST.get('data_obertura')
        saldo = request.POST.get('saldo')
        entidad = request.POST.get('entidad')
        nif = request.POST.get('nif')

        if iban and data_obertura and saldo and entidad and nif:
            client = get_object_or_404(Client, nif=nif)
            Compte.objects.create(iban=iban, data_obertura=data_obertura, saldo=saldo, entidad=entidad, nif=client)
            return redirect('llista_comptes')
    
    clients = Client.objects.all()[:200]  # Mostrar los primeros 200 clients para evitar sobrecargar el formulario
    return render(request, 'afegir_compte.html', {'clients': clients})

def editar_compte(request, iban):
    compte = get_object_or_404(Compte, iban=iban)
    if request.method == 'POST':
        data_obertura = request.POST.get('data_obertura')
        saldo = request.POST.get('saldo')
        entidad = request.POST.get('entidad')
        nif = request.POST.get('nif')

        if data_obertura and saldo and entidad and nif:
            client = get_object_or_404(Client, nif=nif)
            compte.data_obertura = data_obertura
            compte.saldo = saldo
            compte.entidad = entidad
            compte.nif = client
            compte.save()
            return redirect('llista_comptes')
    
    clients = Client.objects.all()[:200]
    return render(request, 'editar_compte.html', {'compte': compte, 'clients': clients})

def eliminar_compte(request, iban):
    compte = get_object_or_404(Compte, iban=iban)
    if request.method == 'POST':
        compte.delete()
        return redirect('llista_comptes')
    
    comptes_list = Compte.objects.all()
    paginator = Paginator(comptes_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'comptes.html', {'page_obj': page_obj})

def llista_operacions(request):
    operacions_list = Operacio.objects.all()
    paginator = Paginator(operacions_list, 25)  # Mostra 25 operacions per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'operacions.html', {'page_obj': page_obj})


def editar_operacio(request, id_operacio):
    operacio = get_object_or_404(Operacio, id_operacio=id_operacio)
    if request.method == 'POST':
        nou_id_operacio = request.POST.get('id_operacio')
        nova_data = request.POST.get('data')
        nou_import = request.POST.get('importt')
        #nou_iban = request.POST.get('iban_origen')
        
        # Asegurar que los inputs no son vacíos
        if nou_id_operacio and nova_data and nou_import:
            if Operacio.objects.filter(id_operacio=nou_id_operacio).exists() and nou_id_operacio != operacio.id_operacio:
                messages.error(request, "El ID de l'operacio ja existeix.")
            else:
                try:
                    #ciutat = get_object_or_404(Ciutat, nom=nom_ciutat)
                    operacio.id_operacio = nou_id_operacio
                    operacio.data = nova_data
                    operacio.importt = nou_import
                    #operacio.iban_origen = nou_iban
                    operacio.save()
                    messages.success(request, "Operacio actualitzada correctament.")
                    return redirect('operacions')
                except Compte.DoesNotExist:
                    messages.error(request, "El compte proporcionat no existeix.")
    return render(request, 'editar_operacio.html', {'operacio': operacio})


def eliminar_operacio(request, id_operacio):
    operacio = get_object_or_404(Operacio, id_operacio=id_operacio)

    if request.method == 'POST':
        try:
            operacio.delete()
            messages.success(request, "Operacio eliminada correctament.")
        except ProtectedError:
            messages.error(request, "No es pot eliminar l'Operacio perquè té sucursals associades.")

        return redirect('operacions')

    return render(request, 'operacions.html', {'operacions': Operacio.objects.all()})


def transferencies(request):
    transferencies_list = Transferencia.objects.all()
    paginator = Paginator(transferencies_list, 25)  # Mostra 25 transferències per pàgina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'transferencies.html', {'page_obj': page_obj})


def buscar_nifs(request):
    if request.is_ajax():
        term = request.GET.get('term', '')
        page = request.GET.get('page', 1)
        clients = Client.objects.filter(nif__icontains=term)
        paginator = Paginator(clients, 10)  # Paginar resultados, 10 por página
        clients_page = paginator.get_page(page)
        results = [{'id': client.nif, 'text': f"{client.nif} - {client.nom}"} for client in clients_page]
        return JsonResponse({'results': results, 'has_next': clients_page.has_next()}, safe=False)
    return JsonResponse([], safe=False)
