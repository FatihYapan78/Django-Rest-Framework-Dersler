# Generated by Django 5.0 on 2024-01-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("haberler", "0006_gazeteci_alter_haber_gazeteci"),
    ]

    operations = [
        migrations.AlterField(
            model_name="haber",
            name="gazeteci",
            field=models.CharField(max_length=50),
        ),
    ]