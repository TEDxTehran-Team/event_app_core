# Generated by Django 3.0.2 on 2020-01-31 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0002_auto_20200131_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventday',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='section',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
    ]
