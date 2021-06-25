# Generated by Django 2.2.4 on 2019-08-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0006_auto_20190816_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour1',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour2',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tape_colour3',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default='70adadb23c714eb1907634eccff455f5', max_length=20),
        ),
    ]