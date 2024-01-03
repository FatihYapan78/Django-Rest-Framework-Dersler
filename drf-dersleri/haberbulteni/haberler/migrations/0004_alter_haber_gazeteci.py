# Generated by Django 5.0 on 2024-01-03 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("haberler", "0003_alter_haber_gazeteci"),
    ]

    operations = [
        migrations.AlterField(
            model_name="haber",
            name="gazeteci",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="haberler",
                to="haberler.gazeteci",
            ),
        ),
    ]