# Generated by Django 2.2 on 2020-04-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200401_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, help_text='a cover image for the album.', null=True, upload_to='', verbose_name='cover'),
        ),
    ]
