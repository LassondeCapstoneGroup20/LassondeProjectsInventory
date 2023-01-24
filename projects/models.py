from django.db import models


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

    name = models.CharField(max_length = 120)
    field = models.CharField(max_length = 60, choices=FIELDS)
    students = models.CharField(max_length = 120, blank = True, default=None)#should this instead use a student model?
    supervisor = models.CharField(max_length = 60, blank = True, default=None)
    date_proposed = models.DateField(auto_now_add = True)
    is_complete = models.BooleanField(default = False)
    date_complete = models.DateField(default=None, blank = True, null = True)
    is_industry_proj = models.BooleanField(default = False)
    industry_partners = models.CharField(max_length = 60, blank = True, default=None)
    cost = models.IntegerField(blank = True, null = True, default = 0)
    notes = models.TextField(blank = True, default=None)
    

