from django.db import models
from datetime import date


# Create your models here.
class AccessLog(models.Model):
    last_accessed = models.DateTimeField(auto_now=True)
    access_count = models.BigIntegerField()

class Project(models.Model):
    FIELDS = [
        ('ELEC', 'Electrical Engineering'),
        ('COMP', 'Computer Engineering'),
        ('SOFT', 'Software Engineering'),
        ('CIVL', 'Civil Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('SPAC', 'Space Engineering'),
        ('GEOM', 'Geomatics Engineering'),
        ('OTHR', 'Other Field'),
    ]

    TYPES = [
        ('COMP', 'Competition'),
        ('LOOSE', 'Loosely Defined'),
        ('WELLDF', 'Well Defined'),
        ('C4', 'C4'),
    ]

    STATUS = [
        ('PROP', 'Proposed but unstarted'),
        ('START', 'Started / In Progress'),
        ('COMPL', 'Completed'),
        ('EXT', 'Completed but Extendable'),
    ]
    name = models.CharField(max_length = 120)
    field = models.CharField(max_length = 30, choices=FIELDS)
    type = models.CharField(max_length = 30, choices=TYPES)
    students = models.CharField(max_length = 120, blank = True, default=None)#should this instead use a student model?
    supervisor = models.CharField(max_length = 60, blank = True, default=None)
    date_proposed = models.DateField(default=date.today)
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0][0])
    date_complete = models.DateField(default=None, blank = True, null = True)
    industry_partners = models.CharField(max_length = 60, blank = True, default=None)
    cost = models.IntegerField(blank = True, null = True, default = 0)
    notes = models.TextField(blank = True, default=None)
    

