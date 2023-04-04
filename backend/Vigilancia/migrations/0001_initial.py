# Generated by Django 4.2 on 2023-04-03 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Servicio', '0001_initial'),
        ('Dependencia', '0001_initial'),
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vigilancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regional', models.CharField(default='', max_length=50)),
                ('motivo', models.CharField(default='', max_length=50)),
                ('objetivo', models.TextField()),
                ('cant_dias', models.IntegerField(blank=True, default=0)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField(null=True)),
                ('destino', models.CharField(max_length=50)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('fk_tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.tiposervicio')),
                ('jurisdiccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='DiasVigilancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateTimeField()),
                ('hora_inicio', models.TimeField(null=True)),
                ('hora_fin', models.TimeField(null=True)),
                ('turno', models.CharField(max_length=100, null=True)),
                ('dia_completo', models.BooleanField(default=False)),
                ('fk_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.personal')),
                ('fk_vigilancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vigilancia.vigilancia')),
            ],
        ),
    ]
