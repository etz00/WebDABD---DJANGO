from django.db import models

#Models a crear

class Ciutat(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'ciutat'
    
    
class OficinaCentral(models.Model):
    id_oficina = models.AutoField(primary_key=True)
    empleats = models.IntegerField()
    nom = models.ForeignKey(Ciutat, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Oficina Central {self.id_oficina}'


class Gestor(models.Model):
    idEmpleat = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    dataInici = models.DateField()

    def __str__(self):
        return self.nom
    
    
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    carrer = models.CharField(max_length=100)
    nom = models.ForeignKey(Ciutat, on_delete=models.RESTRICT)
    id_oficina = models.ForeignKey(OficinaCentral, on_delete=models.RESTRICT)
    id_empleat = models.OneToOneField(Gestor, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Sucursal {self.id_sucursal}'
    
    
class Client(models.Model):
    NIF = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    adreca = models.CharField(max_length=200)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom


class Particular(models.Model):
    NIF = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    ingressos_anuals = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Particular {self.NIF}'


class Empresa(models.Model):
    NIF = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    facturacio = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Empresa {self.NIF}'
    
    
class Compte(models.Model):
    IBAN = models.CharField(max_length=34, primary_key=True)
    data_obertura = models.DateField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    entitat = models.CharField(max_length=100)
    NIF = models.ForeignKey(Client, on_delete=models.RESTRICT)

    def __str__(self):
        return self.IBAN
    
    
class Operacio(models.Model):
    idOperacio = models.AutoField(primary_key=True)
    data = models.DateField()
    IBAN_origen = models.ForeignKey(Compte, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Operacio {self.idOperacio}'


class Efectiu(models.Model):
    idOperacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True)
    quantitat = models.IntegerField()

    def __str__(self):
        return f'Efectiu {self.idOperacio}'


class Transferencia(models.Model):
    idOperacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True)
    IBAN = models.ForeignKey(Compte, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Transferencia {self.idOperacio}'


class CarrecComissions(models.Model):
    idOperacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True)
    import_comissio = models.IntegerField()

    def __str__(self):
        return f'CarrecComissions {self.idOperacio}'


class RelacioTransferencies(models.Model):
    idOperacio = models.OneToOneField(Transferencia, on_delete=models.CASCADE, primary_key=True)
    IBAN = models.ForeignKey(Compte, on_delete=models.RESTRICT)
    suma = models.IntegerField()

    def __str__(self):
        return f'RelacioTransferencies {self.idOperacio}'
