# Generated by Django 3.0.4 on 2020-04-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0038_add_hospital_locations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationdetail',
            name='price_per_piece',
        ),
        migrations.AddField(
            model_name='donationdetail',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Цена в сомах', max_digits=20, verbose_name='Общая стоимость'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donator_type',
            field=models.CharField(choices=[('ORGANIZATION', 'ORGANIZATION'), ('PERSONAL', 'PERSONAL'), ('DONOR', 'DONOR'), ('GOVERNMENT', 'GOVERNMENT')], default='ORGANIZATION', help_text='Выберите тип пожертвования', max_length=12, verbose_name='Тип пожертвования'),
        ),
    ]