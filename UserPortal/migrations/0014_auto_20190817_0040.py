# Generated by Django 2.2.3 on 2019-08-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0013_auto_20190817_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='college',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default='ceec04b82fac43e9811b8a2527604e23', max_length=32),
        ),
    ]
