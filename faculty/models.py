from django.db import models

# Create your models here.
class Faculty(models.Model):
    ROLES = [
        ('PROF', 'Professor'),
        ('TA', 'Teaching Assistant'),
        ('OTHER', 'Other Staff'),
    ]

    DEPTS = [
        ('OTHR', 'Other'),
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
    role = models.CharField(max_length = 5, choices= ROLES, default = ROLES[0][0])
    department = models.CharField(max_length = 4, choices = DEPTS, default = DEPTS[0][0])
    fields_of_interest = models.CharField(max_length = 120, blank = True)
    email = models.CharField(max_length = 40, blank = True)
    notes = models.TextField(blank = True, default = None)

    def __str__(self):
        return ("%s (%s)" %(self.name, self.role))