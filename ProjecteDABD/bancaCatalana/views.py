from django.shortcuts import render
from .models import Ciutat, OficinaCentral, Gestor, Sucursal, Client, Particular, Empresa, Compte, Operacio, Efectiu, Transferencia, CarrecComissions, RelacioTransferencies

def ciutats(request):
    ciutats = Ciutat.objects.all()
    for ciutat in ciutats:
        print(ciutat.nom)
    return render(request, 'ciutats.html', {'ciutats': ciutats})


def oficines_centrals(request):
    oficines = OficinaCentral.objects.all()
    for oficina in oficines:
        print(oficina.nom)
    return render(request, 'oficines_centrals.html', {'oficines': oficines})


def gestors(request):
    gestors = Gestor.objects.all()
    for gestor in gestors:
        print(gestor.nom)
    return render(request, 'gestors.html', {'gestors': gestors})


def sucursals(request):
    sucursals = Sucursal.objects.all()
    #for sucursal in sucursals:
    #    print(sucursal.nom)
    return render(request, 'sucursals.html', {'sucursals': sucursals})


def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def particulars(request):
    particulars = Particular.objects.all()
    for particular in particulars:
        print(particular.NIF)
    return render(request, 'particulars.html', {'particulars': particulars})


def empreses(request):
    empreses = Empresa.objects.all()
    for empresa in empreses:
        print(empresa.NIF)
    return render(request, 'empreses.html', {'empreses': empreses})


def comptes(request):
    comptes = Compte.objects.all()
    for compte in comptes:
        print(compte.IBAN)
    return render(request, 'comptes.html', {'comptes': comptes})


def operacions(request):
    operacions = Operacio.objects.all()
    for operacio in operacions:
        print(operacio.idOperacio)
    return render(request, 'operacions.html', {'operacions': operacions})


def transferencies(request):
    transferencies = Transferencia.objects.all()
    for transferencia in transferencies:
        print(transferencia.idOperacio)
    return render(request, 'transferencies.html', {'transferencies': transferencies})



