# Generated by Django 2.0.2 on 2019-01-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0037_auto_20181108_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catest',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null='True', verbose_name='Relación'),
        ),
    ]
