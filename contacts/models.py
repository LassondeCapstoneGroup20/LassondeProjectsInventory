from django.db import models
from datetime import date


# Create your models here.
class AccessLog(models.Model):
    last_accessed = models.DateTimeField(auto_now=True)
    access_count = models.BigIntegerField()


class IndustryPartners(models.Model):
    FIELDS = [
        ('GOV', 'Government'),
        ('COM', 'For Profit Company'),
        ('FREE', 'Not For Profit'),
    ]

    TYPES = [
        ('GOV', 'Government'),
        ('COM', 'For Profit Company'),
        ('FREE', 'Not For Profit'),
    ]

    STATUS = [
        ('ACT', 'Active Industry Member'),
        ('INACT', 'No Longer an Partner'),
    ]

    name = models.CharField(max_length=120)
    address = models.CharField(max_length=400)
    website = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=30, choices=TYPES)
    date_joined = models.DateField(default=date.today)
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0][0])
    notes = models.TextField(blank=True, default=None)


class Industry_Partners_Projects(models.Model):
    name = models.CharField(max_length=120)
    project_year = models.DateField(default=date.today)

