from django.db import models

#Models a crear

class Ciutat(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'ciutat'


class OficinaCentral(models.Model):
    id_oficina = models.CharField(max_length=100)
    empleats = models.IntegerField()
    nom_ciutat = models.ForeignKey(Ciutat, on_delete=models.CASCADE, db_column='nom_ciutat', null=True)

    def __str__(self):
        return f'Oficina Central {self.id_oficina}'

    class Meta:
        db_table = 'oficina_central'


        

class Gestor(models.Model):
    id_empleat = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    data_inici = models.DateField()

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'gestor'
    
    
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    carrer = models.CharField(max_length=100)
    #nom_ciutat = models.ForeignKey(Ciutat, on_delete=models.RESTRICT, db_column='nom')
    id_oficina = models.ForeignKey(OficinaCentral, on_delete=models.RESTRICT, db_column='id_oficina', default = 0)
    id_empleat = models.OneToOneField(Gestor, on_delete=models.RESTRICT, db_column='id_empleat', unique=True, default=1)

    def __str__(self):
        return f'Sucursal {self.id_sucursal}'

    class Meta:
        db_table = 'sucursal'

    
    
class Client(models.Model):
    nif = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    adreca = models.CharField(max_length=200)
    #id_sucursal = models.ForeignKey(Sucursal, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'client'


class Particular(models.Model):
    #nif = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, db_column='nif')
    ingressos_anuals = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Particular {self.nif}'

    class Meta:
        db_table = 'particular'
        

class Empresa(models.Model):
    nif = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    facturacio = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Empresa {self.nif}'
    
    
class Compte(models.Model):
    iban = models.CharField(max_length=34, primary_key=True)
    data_obertura = models.DateField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    entidad = models.CharField(max_length=100)
    #nif = models.ForeignKey(Client, on_delete=models.RESTRICT)

    def __str__(self):
        return self.iban
    
    class Meta:
        db_table = 'compte'
    
    
class Operacio(models.Model):
    id_operacio = models.AutoField(primary_key=True)
    data = models.DateField()
    #IBAN_origen = models.ForeignKey(Compte, on_delete=models.RESTRICT)

    def __str__(self):
        return f'Operacio {self.id_operacio}'

    class Meta:
        db_table = 'operacio'


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
