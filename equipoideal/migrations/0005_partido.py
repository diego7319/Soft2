# Generated by Django 2.0.1 on 2018-02-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipoideal', '0004_delete_partido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo1', models.CharField(max_length=30)),
                ('equipo2', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('Grupo', models.CharField(max_length=1)),
            ],
        ),
    ]
