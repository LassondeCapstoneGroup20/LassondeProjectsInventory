from datetime import date

from django import forms

from .models import Faculty

class FacultyForm(forms.ModelForm):
  class Meta:
        model = Faculty
        fields = (
            "name",
            "role",
            "department",
            "fields_of_interest",
            "notes",
            )