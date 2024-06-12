# Generated by Django 5.0.6 on 2024-06-12 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bancaCatalana", "0002_alter_oficinacentral_nom_ciutat"),
    ]

    operations = [
        migrations.AddField(
            model_name="oficinacentral",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="oficinacentral",
            name="id_oficina",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="oficinacentral",
            name="nom_ciutat",
            field=models.ForeignKey(
                db_column="nom_ciutat",
                on_delete=django.db.models.deletion.CASCADE,
                to="bancaCatalana.ciutat",
            ),
        ),
    ]