# Generated by Django 5.0.6 on 2024-05-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_galeria_imagens_galeria_imagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='galeria',
        ),
        migrations.AddField(
            model_name='usuario',
            name='galeria',
            field=models.ManyToManyField(to='app.imagem'),
        ),
    ]
