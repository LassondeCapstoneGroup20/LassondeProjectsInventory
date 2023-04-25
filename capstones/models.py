from datetime import date

from django.db import models

from faculty.models import Faculty

# Create your models here.
class Capstone(models.Model):
    starting_year = models.IntegerField(default=date.today().year, primary_key = True)
    teaching_staff = models.ManyToManyField(Faculty, default = None, blank = True, related_name='staff_list')
    teaching_assistants = models.ManyToManyField(Faculty, default = None, blank = True, related_name='ta_list')
    capstone_day = models.DateField(default=None, blank = True, null = True)
    capstone_day_location = models.CharField(max_length = 100, blank = True, default=None)
    capstone_day_judges = models.CharField(max_length = 200, blank = True, default = None)
    teaching_notes = models.TextField(blank = True, default=None)
    other_notes = models.TextField(blank = True, default=None)
    
    def get_staff_list(self):
        return ", ".join([ts.name for ts in self.teaching_staff.all()])
        
    def get_ta_list(self):
        return ", ".join([ta.name for ta in self.teaching_assistants.all()])
    
class Award(models.Model):
    capstone = models.IntegerField(default=date.today().year-1)
    title = models.CharField(max_length = 120)
    project = models.ForeignKey('projects.Project', on_delete = models.SET_NULL, null=True, default=None)
    details = models.TextField(blank = True, default=None)