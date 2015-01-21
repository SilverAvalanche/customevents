# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 1, 20, 22, 57, 18, 418152, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
