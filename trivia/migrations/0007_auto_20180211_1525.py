# Generated by Django 2.0.1 on 2018-02-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0006_salatrivia_scoretrivia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salatrivia',
            name='cantpreguntas',
            field=models.IntegerField(),
        ),
    ]
