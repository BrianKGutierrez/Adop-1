# Generated by Django 4.1.7 on 2023-05-02 12:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personal', '0001_initial'),
        ('Dependencia', '0001_initial'),
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='TurnosVigilancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('turno', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=None)),
                ('hora_inicio', models.TimeField(null=True)),
                ('hora_fin', models.TimeField(null=True)),
                ('diario', models.BooleanField(default=False)),
                ('dia_completo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vigilancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.TextField()),
                ('cant_dias', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField(null=True)),
                ('destino', models.CharField(max_length=50)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('fk_jurisdiccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.dependencia')),
                ('fk_motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vigilancia.motivo')),
                ('fk_tipo_recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.tiporecurso')),
                ('fk_tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.tiposervicio')),
                ('fk_unidad_regional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dependencia.unidadregional')),
                ('turnos_vigilancias', models.ManyToManyField(db_table='vigilancia_turnosvigilancia', default=None, related_name='turnosvigilancia', to='Vigilancia.turnosvigilancia')),
            ],
        ),
        migrations.AddField(
            model_name='turnosvigilancia',
            name='fk_vigilancia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vigilancia.vigilancia'),
        ),
        migrations.CreateModel(
            name='PersonalVigilancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('fk_personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.personal')),
                ('fk_turnoVigilancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vigilancia.turnosvigilancia')),
            ],
        ),
    ]
