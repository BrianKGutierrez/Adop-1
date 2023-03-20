# Generated by Django 4.1.7 on 2023-03-20 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Persona', '0001_initial'),
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('hora', models.TimeField()),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=13)),
                ('cant_protagonistas', models.IntegerField()),
                ('cant_infracciones', models.IntegerField()),
                ('cant_arrestados', models.IntegerField()),
                ('fk_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProcedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_procedimiento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProcedimientoPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detenido', models.BooleanField()),
                ('fk_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Persona.persona')),
                ('fk_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procedimiento.procedimiento')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProcedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_articulo', models.TextField()),
                ('detalle_inciso', models.TextField()),
                ('detalle_tipo_procedimiento', models.TextField()),
                ('detalle_ley', models.TextField()),
                ('fk_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procedimiento.procedimiento')),
                ('fk_tipo_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procedimiento.tipoprocedimiento')),
            ],
        ),
    ]
