# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='processed_by',
            field=models.ForeignKey(related_name='processed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='reviewed_by',
            field=models.ForeignKey(related_name='reviewed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
