# Generated by Django 2.2.4 on 2019-08-28 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0025_auto_20190828_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='custom_currency',
        ),
    ]
