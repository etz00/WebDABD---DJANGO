# Generated by Django 5.0.6 on 2024-06-19 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancaCatalana', '0010_alter_oficinacentral_id_oficina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreccomissions',
            name='id',
        ),
        migrations.AlterField(
            model_name='carreccomissions',
            name='id_operacio',
            field=models.OneToOneField(db_column='id_operacio', default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bancaCatalana.operacio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oficinacentral',
            name='id_oficina',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='RelacioTransferencies',
        ),
    ]
