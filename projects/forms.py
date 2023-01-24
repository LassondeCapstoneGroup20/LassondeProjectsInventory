from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "field",
            "students",
            "supervisor",
            "is_complete",
            "date_complete",
            "is_industry_proj",
            "industry_partners",
            "cost",
            "notes"
            )