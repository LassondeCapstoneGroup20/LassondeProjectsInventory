from django import forms

from .models import EngDiscipline, Project, UNGoals


class MCDisciplineForm(forms.ModelMultipleChoiceField):
    def label_from_instance(self, discipline):
        return discipline.discipline

class MCGoalForm(forms.ModelMultipleChoiceField):
    class Meta:
        labels = {
            'un_goals': "UN Sustainable Development Goals",
        }
    def label_from_instance(self, goal):
        return goal.title

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
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
            "notes"
            )

    discipline = forms.ModelMultipleChoiceField(
        queryset = EngDiscipline.objects.all(),
        widget = forms.CheckboxSelectMultiple
        )
    un_goals = forms.ModelMultipleChoiceField(
        queryset = UNGoals.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        label = 'UN Sustainable Development Goals',
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