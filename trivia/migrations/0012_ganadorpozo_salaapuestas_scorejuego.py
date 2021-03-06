# Generated by Django 2.0.1 on 2018-02-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0011_pagosala'),
    ]

    operations = [
        migrations.CreateModel(
            name='GanadorPozo',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20)),
                ('pago', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalaApuestas',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Scorejuego',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20)),
                ('grupo', models.CharField(max_length=30)),
                ('nombreJuego', models.CharField(max_length=30)),
            ],
        ),
    ]
