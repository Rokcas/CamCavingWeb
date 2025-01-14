# Generated by Django 2.2.4 on 2019-08-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gear', '0014_auto_20190821_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hiresupport',
            options={'managed': False, 'permissions': [('hire_self', 'Can hire gear on their own behalf'), ('hire_other', 'Can hire gear on behalf of others'), ('register_gear', 'Can register gear in the database'), ('view_hires', 'Can view lists of Hire Instances'), ('edit_hires', 'Can edit and delete Hire Instances')]},
        ),
        migrations.AlterField(
            model_name='oversuit',
            name='size',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='undersuit',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]
