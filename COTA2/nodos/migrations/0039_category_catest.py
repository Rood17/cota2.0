# Generated by Django 2.0.2 on 2019-01-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0038_auto_20190113_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catest',
            field=models.ManyToManyField(blank=True, related_name='_category_catest_+', to='nodos.Category', verbose_name='Revisa categorias'),
        ),
    ]
