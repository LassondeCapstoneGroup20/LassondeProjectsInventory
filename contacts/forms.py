from django import forms

from .models import IndustryPartners, Industry_Partners_Projects


class IndustryPartnersForm(forms.ModelForm):
    class Meta:
        model = IndustryPartners
        fields = (
            "name",
            "address",
            "website",
            "phone_number",
            "type",
            "email",
            "date_joined",
            "status",
            "notes"
            )