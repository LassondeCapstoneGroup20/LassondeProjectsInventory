from datetime import date

from django import forms

from .models import EngDiscipline, Project, UNGoals
from faculty.models import Faculty
    
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
    supervisor = forms.ModelChoiceField(queryset = Faculty.objects.filter(role='PROF'))
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