# Generated by Django 2.0.1 on 2018-02-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0013_scorejuego_resultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='notificaciones',
            fields=[
                ('idnotificacion', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=20)),
                ('estado', models.CharField(default='1', max_length=1)),
                ('ganador', models.CharField(default='no', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pozo_sala',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('dinero', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='resultados',
            fields=[
                ('idresultado', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20)),
                ('pago', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='GanadorPozo',
        ),
    ]