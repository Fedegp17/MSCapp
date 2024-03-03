# Generated by Django 5.0.2 on 2024-03-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('address', models.TextField(max_length=300, verbose_name='Dirección')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo del hospital')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
            ],
            options={
                'verbose_name': 'Hospital',
                'verbose_name_plural': 'Hospitales',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellidopaterno', models.CharField(max_length=30, verbose_name='Apellido paterno')),
                ('apellidomaterno', models.CharField(max_length=30, verbose_name='Apellido materno')),
                ('especialidad', models.CharField(max_length=40, verbose_name='Especialidad médica')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellidopaterno', models.CharField(max_length=30, verbose_name='Apellido paterno')),
                ('apellidomaterno', models.CharField(max_length=30, verbose_name='Apellido materno')),
                ('ingreso', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['-ingreso'],
            },
        ),
    ]
