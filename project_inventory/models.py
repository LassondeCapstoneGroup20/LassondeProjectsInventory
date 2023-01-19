from django.db import models

# Create your models here.
class AccessLog(models.Model):
    last_accessed = models.DateTimeField(auto_now=True)
    access_count = models.BigIntegerField()

class Project(models.Model):
    name = models.CharField(max_length = 120)
    students = models.JSONField(blank = True)#should this instead use a student model?
    supervisor = models.JSONField(blank = True)
    date_proposed = models.DateField(auto_now_add = True)
    is_complete = models.BooleanField(default = False)
    date_complete = models.DateField(blank = True)
    is_industry_proj = models.BooleanField(default = False)
    industry_partners = models.JSONField(blank = True)
    notes = models.TextField(blank = True)
    

