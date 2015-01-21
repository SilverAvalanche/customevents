# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrant',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 22, 57, 28, 258248, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
