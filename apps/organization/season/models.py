# models.py- Season
from django.db import models


class Season(models.Model):
    
    #organization Associated
    #teams associated

    seasonTitle = models.TextField(max_length=200, default='')
    seasonStart = models.DateTimeField(auto_now=True, auto_now_add=False, required=True)
    seasonEnd   = models.DateTimeField()




return 
