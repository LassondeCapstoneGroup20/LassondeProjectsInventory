from django.db import models

from contacts.models import Faculty

# Create your models here.

class Faculty(models.Model):
    TYPES = [
        ('PROF', 'Professor'),
        ('TA', 'Teaching Assistant'),
        ('OTHER', 'Other Staff'),
    ]

    DEPTS = [
        ('OTHR', 'Other')
        ('AMPD', 'School of the Arts, Media, Performance & Design'),
        ('ED', 'Faculty of Education'),
        ('FEUC', 'Faculty of Environmental & Urban Change'),
        ('GL', 'Glendon College'),
        ('FGS', 'Faculty of Graduate Studies'),
        ('FH', 'Faculty of Health'),
        ('LSE', 'Lassonde School of Engineering'),
        ('CIVL', 'Civil Engineering'),
        ('ESSE', 'Earth and Space Science and Engineering'),
        ('EECS', 'Electrical Engineering & Computer Science'),
        ('MECH', 'Mechanical Engineering'),
        ('LAPS', 'Faculty of Liberal Arts & Professional Studies'),
        ('OH', 'Osgoode Hall Law School'),
        ('SSB', 'Schulich School of Business'),
        ('SC', 'Faculty of Science'),
    ]

    name = models.CharField(max_length = 120)
    type = models.CharField(max_length = 5, choices= TYPES, default = TYPES[0][0])
    department = models.CharField(max_length = 4, choices = DEPTS, default = DEPTS[0][0])
    fields_of_interest = models.CharField(max_length = 120, blank = True)
    notes = models.TextField(blank = True, default = None)

    
class Capstone(models.Model):
  starting_year = models.DateField(default=date.today)
  teaching_staff = models.ManyToManyField(Faculty, default = None, blank = True)
  teaching_assistants = models.ManyToManyField(Faculty, default = None, blank = True)
  capstone_day = models.DateField(default=None, blank = True, null = True)
  capstone_day_location = models.CharField(max_length = 100, blank = True, default=None)
  capstone_day_judges = models.CharField(max_length = 200, blank = True, default = None)
  teaching_notes = models.TextField(blank = True, default=None)
  other_notes = models.TextField(blank = True, default=None)

  