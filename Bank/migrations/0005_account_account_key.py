# Generated by Django 2.2.4 on 2019-08-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0004_auto_20190822_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_key',
            field=models.CharField(default='65b2a2bff51c49299f58f6b9ca0f2b35', max_length=32),
        ),
    ]