# Generated by Django 5.0.6 on 2024-06-10 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Operacio",
            fields=[
                ("idOperacio", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Ciutat",
            fields=[
                (
                    "nom",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "NIF",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(max_length=100)),
                ("telefon", models.CharField(max_length=20)),
                ("adreca", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Compte",
            fields=[
                (
                    "IBAN",
                    models.CharField(max_length=34, primary_key=True, serialize=False),
                ),
                ("data_obertura", models.DateField()),
                ("saldo", models.DecimalField(decimal_places=2, max_digits=15)),
                ("entitat", models.CharField(max_length=100)),
                (
                    "NIF",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gestor",
            fields=[
                ("idEmpleat", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=100)),
                ("dataInici", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="CarrecComissions",
            fields=[
                (
                    "idOperacio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.operacio",
                    ),
                ),
                ("import_comissio", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Efectiu",
            fields=[
                (
                    "idOperacio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.operacio",
                    ),
                ),
                ("quantitat", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Transferencia",
            fields=[
                (
                    "idOperacio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.operacio",
                    ),
                ),
                (
                    "IBAN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.compte",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Empresa",
            fields=[
                (
                    "NIF",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.client",
                    ),
                ),
                ("facturacio", models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name="Particular",
            fields=[
                (
                    "NIF",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.client",
                    ),
                ),
                (
                    "ingressos_anuals",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
            ],
        ),
        migrations.AddField(
            model_name="operacio",
            name="IBAN_origen",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="bancaCatalana.compte"
            ),
        ),
        migrations.CreateModel(
            name="OficinaCentral",
            fields=[
                ("id_oficina", models.AutoField(primary_key=True, serialize=False)),
                ("empleats", models.IntegerField()),
                (
                    "nom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.ciutat",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sucursal",
            fields=[
                ("id_sucursal", models.AutoField(primary_key=True, serialize=False)),
                ("carrer", models.CharField(max_length=100)),
                (
                    "id_empleat",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.gestor",
                    ),
                ),
                (
                    "id_oficina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.oficinacentral",
                    ),
                ),
                (
                    "nom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.ciutat",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="client",
            name="id_sucursal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="bancaCatalana.sucursal",
            ),
        ),
        migrations.CreateModel(
            name="RelacioTransferencies",
            fields=[
                (
                    "idOperacio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="bancaCatalana.transferencia",
                    ),
                ),
                ("suma", models.IntegerField()),
                (
                    "IBAN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="bancaCatalana.compte",
                    ),
                ),
            ],
        ),
    ]