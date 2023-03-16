# Generated by Django 3.2.10 on 2023-03-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.BigIntegerField(primary_key=True, serialize=False)),
                ('profesion', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=8)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
    ]
