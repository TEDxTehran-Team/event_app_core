# Generated by Django 2.2 on 2020-10-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsors',
            name='event',
            field=models.ManyToManyField(blank=True, help_text='to which event does the sponsor belong?', related_name='sponsors', to='events.Event', verbose_name='event'),
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='organizer',
            field=models.ManyToManyField(blank=True, help_text='to which organizer does the sponsor belong?', related_name='sponsors', to='organizers.Organizer', verbose_name='organizer'),
        ),
    ]
