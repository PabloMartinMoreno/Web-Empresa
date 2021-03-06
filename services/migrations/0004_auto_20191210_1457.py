# Generated by Django 2.2.7 on 2019-12-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20191201_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitulo')),
                ('content', models.TextField(max_length=500, verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
