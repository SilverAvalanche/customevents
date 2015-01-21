# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '__first__'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start', models.DateTimeField(auto_now=True)),
                ('end', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('organization', models.ForeignKey(to='organization.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeasonTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.ForeignKey(to='season.Season')),
                ('team', models.ForeignKey(to='team.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='season',
            name='seasonTeams',
            field=models.ManyToManyField(to='team.Team', through='season.SeasonTeam'),
            preserve_default=True,
        ),
    ]
