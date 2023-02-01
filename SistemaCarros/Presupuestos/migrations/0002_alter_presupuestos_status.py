# Generated by Django 3.2.10 on 2022-06-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestos',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('CANCELED', 'canceled'), ('PAID', 'paid')], default='PENDING', max_length=10),
        ),
    ]