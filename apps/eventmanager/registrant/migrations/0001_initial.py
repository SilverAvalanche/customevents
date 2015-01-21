# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fName', models.CharField(default=b'John', max_length=100)),
                ('lName', models.CharField(default=b'Doe', max_length=100)),
                ('email', models.EmailField(default=b'example@example.com', max_length=100)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
