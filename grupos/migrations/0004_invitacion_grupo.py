# Generated by Django 2.0.1 on 2018-01-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0003_remove_invitacion_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitacion',
            name='grupo',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]