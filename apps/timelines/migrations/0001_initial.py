# Generated by Django 3.0.2 on 2020-01-31 11:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20200130_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('date', models.DateField(help_text='the date of this event day.', verbose_name='date')),
                ('event', models.ForeignKey(help_text='to which event does the day belong?', on_delete=django.db.models.deletion.CASCADE, related_name='days', to='events.Event', verbose_name='event')),
            ],
            options={
                'verbose_name': 'event day',
                'verbose_name_plural': 'event days',
                'ordering': ['event', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('start_time', models.TimeField(help_text='when will the session start?', verbose_name='start time')),
                ('end_time', models.TimeField(help_text='when will the session end?', verbose_name='end time')),
                ('image', models.ImageField(blank=True, help_text='an optional logo or thumbnail related to the session.', null=True, upload_to='', verbose_name='image')),
                ('day', models.ForeignKey(help_text='to which event day does this session belong?', on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='timelines.EventDay', verbose_name='day')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'ordering': ['day', 'start_time', 'end_time'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('start_time', models.TimeField(help_text='when will the section start?', verbose_name='start time')),
                ('end_time', models.TimeField(help_text='when will the section end?', verbose_name='end time')),
                ('image', models.ImageField(blank=True, help_text='an optional logo or thumbnail related to the section.', null=True, upload_to='', verbose_name='image')),
                ('type', models.CharField(choices=[('generic', 'Generic'), ('talk', 'Talks'), ('performance', 'Performance'), ('activity', 'Activity'), ('entertainment', 'Entertainment')], default='generic', help_text="shows type of this program section, whether it's a generic section, a talk or performance, an activity, or else.", max_length=31, verbose_name='type')),
                ('event', models.ForeignKey(help_text='to which event does the section belong?', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='events.Event', verbose_name='event')),
                ('sessions', models.ManyToManyField(help_text='in which session(s) this section will be held?', related_name='sections', to='timelines.Session', verbose_name='sessions')),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ['event', 'start_time', 'end_time'],
            },
        ),
    ]
