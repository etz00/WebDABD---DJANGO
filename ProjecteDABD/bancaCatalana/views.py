from django.shortcuts import render
from .models import Ciutat, OficinaCentral, Gestor, Sucursal, Client, Particular, Empresa, Compte, Operacio, Efectiu, Transferencia, CarrecComissions, RelacioTransferencies

def ciutats(request):
    ciutats = Ciutat.objects.all()
    for ciutat in ciutats:
        print(ciutat.nom)
    return render(request, 'ciutats.html', {'ciutats': ciutats})

