# Generated by Django 2.0.2 on 2018-07-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0008_auto_20180723_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Categoria de estudio')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias de estudio',
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_estudio',
        ),
        migrations.AddField(
            model_name='category',
            name='categorias_estudio',
            field=models.ManyToManyField(related_name='get_nodos', to='nodos.CategoryStudy', verbose_name='Categorias de estudio'),
        ),
    ]
