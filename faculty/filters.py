import django_filters
from .models import Faculty

class FacultyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    fields_of_interest = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Faculty
        fields = {
            'role':['exact'],
            'department':['exact'],
        }