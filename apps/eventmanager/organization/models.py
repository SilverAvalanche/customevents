# models.py- Organizaton

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    deleted = models.BooleanField(default=False, db_index=True)
    

    @property
    def delete(self):
        self.deleted = True
        self.save()
    
    def is_active(self):
        if (self.deleted == False):
            return True
        return False



