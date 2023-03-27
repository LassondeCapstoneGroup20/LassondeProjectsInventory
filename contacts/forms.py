from django import forms

from .models import IndustryPartners, Industry_Partners_Projects
from projects.models import EngDiscipline


class IndustryPartnersForm(forms.ModelForm):
    class Meta:
        model = IndustryPartners
        fields = (
            "name",
            "address",
            "website",
            "discipline"
            "phone_number",
            "type",
            "email",
            "date_joined",
            "status",
            "notes"
            )

    discipline = forms.ModelMultipleChoiceField(
        queryset=EngDiscipline.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        error_messages={'required': 'Please select at least 1 discipline'},
        required=False,
    )