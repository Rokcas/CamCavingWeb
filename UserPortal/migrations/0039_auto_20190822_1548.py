# Generated by Django 2.2.4 on 2019-08-22 14:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserPortal', '0038_auto_20190822_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_key',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100),
        ),
    ]