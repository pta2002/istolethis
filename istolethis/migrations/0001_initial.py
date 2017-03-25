# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(default=uuid.uuid4, max_length=36)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(default='Untitled', max_length=256)),
                ('until', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='GameText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='istolethis.Game')),
            ],
        ),
    ]
