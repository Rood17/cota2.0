# Generated by Django 2.0.2 on 2018-10-13 17:33

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0031_auto_20181013_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pais',
            field=models.CharField(default='México', max_length=20, verbose_name='País y/o Edo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='periodo',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('00', '1900'), ('10', '1910'), ('20', '1920'), ('30', '1930'), ('40', '1940'), ('50', '1950'), ('60', '1960'), ('70', '1970'), ('80', '1980'), ('90', '1990'), ('2m', '2000'), ('21', '2010'), ('22', '2020')], default='2m', max_length=1, verbose_name='Periódo de tiempo'),
        ),
    ]
