import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    cost = django_filters.RangeFilter()
    class Meta:
        model = Project
        fields = {
            'id':['exact'],
            'name':['icontains'],
            'discipline':['exact'],
            'type':['exact'],
            'capstone_year':['exact'],
            'supervisor':['exact'],
            'status':['exact'],
            'un_goals':['exact'],
            'tags':['icontains'],
            }