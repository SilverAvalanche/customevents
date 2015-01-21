# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamName', models.CharField(max_length=100)),
                ('teamLeaderEmail', models.EmailField(default=b'teamleader@teamleader.com', max_length=75)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamRegistrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registrant', models.ForeignKey(to='registrant.Registrant')),
                ('team', models.ForeignKey(to='team.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='teamMembers',
            field=models.ManyToManyField(to='registrant.Registrant', through='team.TeamRegistrant'),
            preserve_default=True,
        ),
    ]
