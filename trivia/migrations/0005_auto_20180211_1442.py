# Generated by Django 2.0.1 on 2018-02-11 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0004_salatrivia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='salatrivia',
        ),
        migrations.DeleteModel(
            name='scoretrivia',
        ),
    ]
