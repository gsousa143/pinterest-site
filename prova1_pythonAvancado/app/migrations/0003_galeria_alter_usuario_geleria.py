# Generated by Django 5.0.6 on 2024-05-23 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_usuario_delete_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.imagem')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='geleria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.galeria'),
        ),
    ]
