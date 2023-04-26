from django import forms

from .models import IndustryPartners
from django.apps import apps

class IndustryPartnersForm(forms.ModelForm):
    class Meta:
        model = IndustryPartners
        fields = (
            "name",
            "address",
            "website",
            "discipline",
            "phone_number",
            "type",
            "email",
            "date_joined",
            "status",
            "notes"
            )

    discipline = forms.ModelMultipleChoiceField(
        queryset=apps.get_model("projects.EngDiscipline").objects.all(),
        widget=forms.CheckboxSelectMultiple,
        error_messages={'required': 'Please select at least 1 discipline'},
        required=False,
    )

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = apps.get_model("projects.EngDiscipline")
        fields = (
            "discipline",
            )