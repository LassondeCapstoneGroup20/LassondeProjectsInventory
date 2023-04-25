import django_filters
from .models import Project
#attrs={'style':'width: 50px'}

class ProjectFilter(django_filters.FilterSet):
    cost = django_filters.NumericRangeFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Project
        fields = {
            'id':['exact'],
            'discipline':['exact'],
            'type':['exact'],
            'capstone_year':['exact'],
            'supervisor':['exact'],
            'status':['exact'],
            'un_goals':['exact'],
            }