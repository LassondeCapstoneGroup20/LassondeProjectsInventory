from datetime import date

from django import forms

from .models import EngDiscipline, Project, UNGoals
from faculty.models import Faculty
from contacts.models import IndustryPartners
    
class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "capstone_year",
            "discipline",
            "type",
            "students",
            "supervisor",
            "date_proposed",
            "status",
            "date_complete",
            "industry_partners",
            "cost",
            "un_goals",
            "tags",
            "notes"
            )
    date_proposed = forms.DateField(widget=DateInput, initial = date.today())
    date_complete = forms.DateField(widget=DateInput, required = False)
    supervisor = forms.ModelMultipleChoiceField(
        queryset = Faculty.objects.filter(role = 'PROF').order_by('department', 'name'), 
        widget = forms.SelectMultiple(attrs={'class':'form-control', 'style':'height: 200px'}),
        label = 'Supervisor (hold control to select/unselect multiple)',
        required = False,
    )
    discipline = forms.ModelMultipleChoiceField(
        queryset = EngDiscipline.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        error_messages = {'required': 'Please select at least 1 discipline'},
        required = True,
    )
    un_goals = forms.ModelMultipleChoiceField(
        queryset = UNGoals.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        label = 'UN Sustainable Development Goals',
        required = False,
    )
    industry_partners = forms.ModelChoiceField(queryset = IndustryPartners.objects.all(), required = False)

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = EngDiscipline
        fields = (
            "discipline",
            )

class GoalForm(forms.ModelForm):
    class Meta:
        model = UNGoals
        fields = (
            "id",
            "title",
            "description",
            "link",
        )

class ProjectsImportForm(forms.Form):
    file = forms.FileField()