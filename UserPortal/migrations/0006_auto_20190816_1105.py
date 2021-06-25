# Generated by Django 2.2.4 on 2019-08-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0005_auto_20190816_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tape_colour1',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='black', max_length=6),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tape_colour2',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='black', max_length=6),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tape_colour3',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('red', 'RED'), ('orange', 'ORANGE'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('blue', 'BLUE'), ('purple', 'PURPLE'), ('grey', 'GREY'), ('white', 'WHITE'), ('earth', 'EARTH'), ('other', 'OTHER')], default='black', max_length=6),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tape_colour_notes',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default='d68663b97c4342b9af5046944bf32b24', max_length=20),
        ),
    ]