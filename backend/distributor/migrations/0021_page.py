# Generated by Django 3.0.4 on 2020-03-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0020_auto_20200328_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('url', models.CharField(max_length=200, verbose_name='Url')),
                ('content', models.TextField(max_length=1000, verbose_name='Content')),
                ('content_ru', models.TextField(max_length=1000, null=True, verbose_name='Content')),
                ('content_ky', models.TextField(max_length=1000, null=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
