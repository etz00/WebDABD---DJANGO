from django.db import models

class Ciutat(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'ciutat'

class OficinaCentral(models.Model):
    id_oficina = models.CharField(max_length=20, primary_key=True)  # Asegúrate de especificar el max_length
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
    nom_ciutat = models.ForeignKey(Ciutat, on_delete=models.RESTRICT, db_column='nom_ciutat')
    id_oficina = models.ForeignKey(OficinaCentral, on_delete=models.RESTRICT, db_column='id_oficina')
    id_empleat = models.OneToOneField(Gestor, on_delete=models.RESTRICT, db_column='id_empleat', unique=True)

    def __str__(self):
        return f'Sucursal {self.id_sucursal}'

    class Meta:
        db_table = 'sucursal'

class Client(models.Model):
    nif = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    adreca = models.CharField(max_length=200)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.RESTRICT, db_column='id_sucursal')

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'client'

class Particular(models.Model):
    nif = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, db_column='nif')
    ingressos_anuals = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Particular {self.nif}'

    class Meta:
        db_table = 'particular'

class Empresa(models.Model):
    nif = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, db_column='nif')
    facturacio = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Empresa {self.nif}'

    class Meta:
        db_table = 'empresa'

class Compte(models.Model):
    iban = models.CharField(max_length=34, primary_key=True)
    data_obertura = models.DateField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    entidad = models.CharField(max_length=100)
    nif = models.ForeignKey(Client, on_delete=models.RESTRICT, db_column='nif')

    def __str__(self):
        return self.iban
    
    class Meta:
        db_table = 'compte'

class Operacio(models.Model):
    id_operacio = models.AutoField(primary_key=True)
    data = models.DateField()
    import_real = models.DecimalField(max_digits=15, decimal_places=2)
    IBAN_origen = models.ForeignKey(Compte, on_delete=models.RESTRICT, db_column='IBAN_origen')

    def __str__(self):
        return f'Operacio {self.id_operacio}'

    class Meta:
        db_table = 'operacio'

class Efectiu(models.Model):
    id_operacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True, db_column='id_operacio')
    quantitat = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Efectiu {self.id_operacio}'

    class Meta:
        db_table = 'efectiu'

class Transferencia(models.Model):
    id_operacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True, db_column='id_operacio')
    IBAN_desti = models.ForeignKey(Compte, on_delete=models.RESTRICT, db_column='IBAN_desti')
    import_real = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'Transferencia {self.id_operacio}'

    class Meta:
        db_table = 'transferencia'

class CarrecComissions(models.Model):
    id_operacio = models.OneToOneField(Operacio, on_delete=models.CASCADE, primary_key=True, db_column='id_operacio')
    import_real = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'CarrecComissions {self.id_operacio}'

    class Meta:
        db_table = 'carrec_comissions'
