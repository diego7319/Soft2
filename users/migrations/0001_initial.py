# Generated by Django 2.0.1 on 2018-02-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuariocuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('dinerocuenta', models.FloatField(default=0)),
            ],
        ),
    ]
