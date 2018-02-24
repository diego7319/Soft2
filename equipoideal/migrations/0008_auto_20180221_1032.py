# Generated by Django 2.0.1 on 2018-02-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipoideal', '0007_salatrivia'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoSalaEquipoIdeal',
            fields=[
                ('idjuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20)),
                ('estadopago', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='salatrivia',
            new_name='salaequipoideal',
        ),
    ]