# Generated by Django 5.0.6 on 2024-05-23 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_galeria_alter_usuario_geleria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='geleria',
            new_name='galeria',
        ),
    ]
