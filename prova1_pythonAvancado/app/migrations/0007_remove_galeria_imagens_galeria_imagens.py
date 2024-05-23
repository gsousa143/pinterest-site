# Generated by Django 5.0.6 on 2024-05-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_usuario_galeria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='imagens',
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagens',
            field=models.ManyToManyField(to='app.imagem'),
        ),
    ]
