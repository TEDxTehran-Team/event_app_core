# Generated by Django 3.0.2 on 2020-01-30 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_by',
            field=models.ForeignKey(default=1, help_text='who has created the link?', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
    ]
