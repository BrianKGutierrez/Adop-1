# Generated by Django 4.1.7 on 2023-04-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Procedimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ley', models.TextField()),
                ('fk_tipo_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procedimiento.tipoprocedimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Inciso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inciso', models.TextField()),
                ('fk_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ley.articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='fk_ley',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ley.ley'),
        ),
    ]
