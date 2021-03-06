# Generated by Django 2.0.1 on 2018-02-12 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0008_auto_20180211_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoSala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20)),
                ('estadopago', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='salatrivia',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('cantpreguntas', models.IntegerField()),
                ('estado', models.CharField(max_length=11)),
                ('pago', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='scoretrivia',
            fields=[
                ('idtrivia', models.AutoField(primary_key=True, serialize=False)),
                ('grupo', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20)),
                ('sala', models.CharField(max_length=20)),
                ('puntaje', models.FloatField()),
                ('idjueg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.salatrivia')),
            ],
        ),
    ]
