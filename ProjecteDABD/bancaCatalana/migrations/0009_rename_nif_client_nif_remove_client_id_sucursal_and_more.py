# Generated by Django 5.0.6 on 2024-06-12 15:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bancaCatalana", "0008_remove_sucursal_id_empleat_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="NIF",
            new_name="nif",
        ),
        migrations.RemoveField(
            model_name="client",
            name="id_sucursal",
        ),
        migrations.AlterModelTable(
            name="client",
            table="client",
        ),
    ]