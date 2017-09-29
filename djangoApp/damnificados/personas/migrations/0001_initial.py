# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=180)),
                ('edad', models.IntegerField(max_length=3)),
                ('sexo', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre'), ('I', 'Indefinido')], max_length=5)),
                ('tipo_de_personas', models.CharField(choices=[('D', 'Damnificado'), ('Voluntario', 'Voluntario'), ('Otro', 'Otro')], max_length=50)),
            ],
        ),
    ]
