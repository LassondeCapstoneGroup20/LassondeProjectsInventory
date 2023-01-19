from django.db import models

# Create your models here.
class AccessLog(models.Model):
    last_accessed = models.DateTimeField(auto_now=True)
    access_count = models.BigIntegerField()