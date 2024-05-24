# Generated by Django 5.0.6 on 2024-05-24 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_usuario_galeria_usuario_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.imagem')),
            ],
        ),
        migrations.DeleteModel(
            name='Galeria',
        ),
    ]
