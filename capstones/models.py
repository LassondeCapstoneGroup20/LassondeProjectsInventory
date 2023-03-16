from datetime import date

from django.db import models

from faculty.models import Faculty

# Create your models here.

class Capstone(models.Model):
  starting_year = models.IntegerField(default=date.today().year)
  teaching_staff = models.ManyToManyField(Faculty, default = None, blank = True)
  teaching_assistants = models.ManyToManyField(Faculty, default = None, blank = True)
  capstone_day = models.DateField(default=None, blank = True, null = True)
  capstone_day_location = models.CharField(max_length = 100, blank = True, default=None)
  capstone_day_judges = models.CharField(max_length = 200, blank = True, default = None)
  teaching_notes = models.TextField(blank = True, default=None)
  other_notes = models.TextField(blank = True, default=None)

  