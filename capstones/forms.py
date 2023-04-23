from datetime import date

from django import forms

from .models import Capstone, Faculty, Award
from projects.models import Project

class DateInput(forms.DateInput):
    input_type = 'date'

class CapstoneForm(forms.ModelForm):
  class Meta:
        model = Capstone
        fields = (
            "starting_year",
            "teaching_staff",
            "teaching_assistants",
            "capstone_day",
            "capstone_day_location",
            "capstone_day_judges",
            "teaching_notes",
            "other_notes",
            )
  capstone_day = forms.DateField(widget=DateInput, required = False)
  teaching_staff = forms.ModelMultipleChoiceField(
      queryset = Faculty.objects.filter(role = "PROF"),
      widget = forms.CheckboxSelectMultiple,
      required = False,
  )
  teaching_assistants = forms.ModelMultipleChoiceField(
      queryset = Faculty.objects.filter(role = "TA"),
      widget = forms.CheckboxSelectMultiple,
      required = False,
  )

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields=(
            'capstone',
            'title',
            'project',
            'details',
        )