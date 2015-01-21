# models.py- Team

from django.db import models
from apps.eventmanager.registrant.models import * #Registrant


class Team(models.Model):
    teamName = models.CharField(max_length=100)
    teamLeaderEmail = models.EmailField(max_length=75,default='teamleader@teamleader.com') # required if team leader
    deleted = models.BooleanField(default=False, db_index=True)
    teamMembers = models.ManyToManyField(Registrant, through='TeamRegistrant', through_fields=('team','registrant'))     
    @property
    def delete(self):
        self.deleted = True
        self.save()

    def is_active(self):
        if(self.deleted == False):
            return True
        return False

class TeamRegistrant(models.Model):
    registrant = models.ForeignKey(Registrant)
    team = models.ForeignKey(Team)
