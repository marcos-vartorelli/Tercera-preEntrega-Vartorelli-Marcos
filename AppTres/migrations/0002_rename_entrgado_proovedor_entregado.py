# Generated by Django 4.2.2 on 2023-07-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTres', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proovedor',
            old_name='entrgado',
            new_name='entregado',
        ),
    ]