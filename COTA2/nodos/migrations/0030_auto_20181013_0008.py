# Generated by Django 2.0.2 on 2018-10-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0029_auto_20181011_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='periodo',
            field=models.CharField(choices=[('00', '1900'), ('10', '1910'), ('20', '1920'), ('30', '1930'), ('40', '1940'), ('50', '1950'), ('60', '1960'), ('70', '1970'), ('80', '1980'), ('90', '1990'), ('2m', '2000'), ('21', '2010'), ('22', '2020')], default='2m', max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Año de edición'),
        ),
    ]
