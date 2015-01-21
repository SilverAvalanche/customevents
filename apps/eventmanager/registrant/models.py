# models.py- Registrant
from django.contrib.auth.models import User
from django.db import models
from apps.eventmanager.team.models import * #includes Team, TeamRegistrant (Thru table) 
from pygment.lexers import get_all_lexers, get_lexer_by_name
from pygments import highlight
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter


#TODO PAYMENTS

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0,] item[0]) for item in LEXERS]i)
STYLE_CHOICES = sorted((item, item) for item in get_all_styles()) 


class Registrant(models.Model):
    fName = models.CharField(max_length=100, default='John')
    lName = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(max_length=100, default='example@example.com')
    created = models.DateTimeField(auto_now=True, auto_now_add=True )        
    deleted = models.BooleanField(default=False, db_index=True)
   
    #Rest  
    code = models.TextField()
    linenos = models.BooleanField(default=True)
    language = models.CharField(default='python', max_length=100)


    @property
    def delete(self):
        self.deleted = True
        self.save()
    
    def is_active(self):
        if (self.deleted == False):
            return True
        return False
    def get_payments(self):
        return self.payment_set.all()
        
