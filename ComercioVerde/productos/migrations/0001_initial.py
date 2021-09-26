# Generated by Django 3.2.7 on 2021-09-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hogar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('Precio', models.FloatField(blank=True, max_length=7, null=True)),
                ('Descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('Unidad', models.CharField(blank=True, max_length=100, null=True)),
                ('Cantidad', models.FloatField(blank=True, max_length=100, null=True)),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='producto')),
                ('Fechaelaboracion', models.DateField(blank=True, null=True)),
                ('Fechavencimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('Precio', models.FloatField(blank=True, max_length=7, null=True)),
                ('Descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('Unidad', models.CharField(blank=True, max_length=100, null=True)),
                ('Cantidad', models.FloatField(blank=True, max_length=100, null=True)),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='producto')),
                ('Fechaelaboracion', models.DateField(blank=True, null=True)),
                ('Fechavencimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='saludybelleza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('Precio', models.FloatField(blank=True, max_length=7, null=True)),
                ('Descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('Unidad', models.CharField(blank=True, max_length=100, null=True)),
                ('Cantidad', models.FloatField(blank=True, max_length=100, null=True)),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='producto')),
                ('Fechaelaboracion', models.DateField(blank=True, null=True)),
                ('Fechavencimiento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
