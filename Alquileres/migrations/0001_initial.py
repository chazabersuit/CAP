# Generated by Django 4.1.7 on 2023-04-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquileres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('cuit', models.IntegerField()),
                ('direccion', models.CharField(max_length=30)),
                ('inicio_contrato', models.DateField()),
            ],
        ),
    ]
