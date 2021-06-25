# Generated by Django 2.2.3 on 2019-08-20 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gear', '0005_auto_20190820_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hireharness',
            name='signed_out_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hireharnessigned_out', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hirehelmet',
            name='signed_out_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hirehelmetigned_out', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hiresrtkit',
            name='signed_out_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiresrtkitigned_out', to=settings.AUTH_USER_MODEL),
        ),
    ]