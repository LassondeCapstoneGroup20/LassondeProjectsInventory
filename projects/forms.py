from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "field",
            "type",
            "students",
            "supervisor",
            "date_proposed",
            "status",
            "date_complete",
            "industry_partners",
            "cost",
            "notes"
            )