# Generated by Django 3.0.4 on 2020-03-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0021_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='search_district_id',
            field=models.IntegerField(null=True, verbose_name='Search District ID'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='search_locality_id',
            field=models.IntegerField(null=True, verbose_name='Search Locality ID'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='search_region_id',
            field=models.IntegerField(null=True, verbose_name='Search Region ID'),
        ),
    ]
