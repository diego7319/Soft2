# Generated by Django 2.0.1 on 2018-02-05 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_scoretrivia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='scoretrivia',
        ),
    ]