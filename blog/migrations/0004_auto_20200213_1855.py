# Generated by Django 2.2.7 on 2020-02-13 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191225_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 13, 18, 55, 41, 977972, tzinfo=utc), verbose_name='Fecha de edición'),
        ),
    ]
