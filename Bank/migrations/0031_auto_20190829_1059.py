# Generated by Django 2.2.4 on 2019-08-29 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0030_auto_20190829_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'permissions': [('approve__entry', 'Can approve entries')]},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': [('approve__event', 'Can approve events')]},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'permissions': [('approve__transaction', 'Can approve transactions')]},
        ),
        migrations.AlterModelOptions(
            name='transactiongroup',
            options={'permissions': [('approve__transaction_group', 'Can approve transaction groups')]},
        ),
    ]