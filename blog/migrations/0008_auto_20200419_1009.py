# Generated by Django 2.2 on 2020-04-19 10:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200308_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 10, 9, 35, 240608, tzinfo=utc), verbose_name='Fecha de edición'),
        ),
    ]
