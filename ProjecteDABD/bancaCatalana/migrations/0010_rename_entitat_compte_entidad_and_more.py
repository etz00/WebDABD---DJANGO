# Generated by Django 5.0.6 on 2024-06-12 20:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "bancaCatalana",
            "0009_rename_nif_client_nif_remove_client_id_sucursal_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="compte",
            old_name="entitat",
            new_name="entidad",
        ),
        migrations.RenameField(
            model_name="compte",
            old_name="IBAN",
            new_name="iban",
        ),
        migrations.RemoveField(
            model_name="compte",
            name="NIF",
        ),
        migrations.AlterModelTable(
            name="compte",
            table="compte",
        ),
    ]
