# Generated by Django 2.0.2 on 2018-08-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0017_auto_20180802_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categorias_estudio',
        ),
    ]
