# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('status', models.CharField(default=b'OPEN', max_length=10, choices=[(b'OPEN', 'Open'), (b'PROCESSED', 'Processed'), (b'REVIEWED', 'Reviewed')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('last_auditor', models.ForeignKey(related_name='last_auditor', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
