from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from contacts.models import IndustryPartners
from faculty.models import Faculty

# Create your models here.
class EngDiscipline(models.Model):
    '''
    Examples
    FIELDS = [
        ('ELEC', 'Electrical Engineering'),
        ('COMP', 'Computer Engineering'),
        ('SOFT', 'Software Engineering'),
        ('CIVL', 'Civil Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('SPAC', 'Space Engineering'),
        ('GEOM', 'Geomatics Engineering'),
        ('OTHR', 'Other Field'),
    ]'''
    discipline = models.CharField(max_length = 30)

    def __str__(self):
        return self.discipline

class UNGoals(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return ("%s: %s" %(self.id, self.title))

class Project(models.Model):
    TYPES = [
        ('COMP', 'Competition'),
        ('LOOSE', 'Loosely Defined'),
        ('WELLDF', 'Well Defined'),
        ('C4', 'C4'),
    ]

    STATUS = [
        ('NOTRDY', 'Missing Project Details'),
        ('PROP', 'Proposed / Unstarted'),
        ('START', 'Started / In Progress'),
        ('COMPL', 'Completed'),
        ('EXT', 'Completed / Extendable'),
    ]
    name = models.CharField(max_length = 120)
    capstone_year = models.IntegerField(default = date.today().year)
    discipline = models.ManyToManyField(EngDiscipline)
    type = models.CharField(max_length = 6, choices=TYPES)
    source = models.CharField(max_length = 30, null = True)
    students = models.CharField(max_length = 120, blank = True, default=None)
    supervisor = models.ManyToManyField('faculty.Faculty', blank = True, default = None)
    date_proposed = models.DateField(default=date.today)
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0][0])
    date_complete = models.DateField(default=None, blank = True, null = True)
    industry_partners = models.ForeignKey('contacts.IndustryPartners', null = True, default=None, on_delete=models.SET_NULL)
    cost = models.IntegerField(blank = True, null = True, default = 0)
    un_goals = models.ManyToManyField(UNGoals, default = None, blank = True)
    tags = models.CharField(max_length = 120, blank = True)
    notes = models.TextField(blank = True, default=None)
    file_report = models.FileField(default=None,blank=True, upload_to='projects/static/upload/')
    file_capstone = models.FileField(default=None, blank=True, upload_to='projects/static/upload/')
    file_mini_capstone = models.FileField(default=None, blank=True, upload_to='projects/static/upload/')
    file_project_trailer = models.FileField(default=None, blank=True, upload_to='projects/static/upload/')

    def get_disciplines(self):
        return "\n".join([d.discipline for d in self.discipline.all()])

    def get_goals(self):
        return "\n".join([str(g.id) +": "+ g.title for g in self.un_goals.all()])

    def get_partner_name(self):
        return self.industry_partners.name

    def get_supervisors(self):
        return "\n".join([s.__str__() for s in self.supervisor.all()])
    
    def __str__(self):
        return ("Proj %i: %s (%s)" %(self.id, self.name, self.capstone_year))
