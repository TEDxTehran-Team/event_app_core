# Generated by Django 3.0.2 on 2020-01-30 11:41

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizer',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='organizer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='organizeraccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizeraccount',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='organizeraccount',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='organizeraccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]
