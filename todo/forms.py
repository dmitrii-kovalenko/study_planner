import datetime
from django import forms
from django.forms.models import inlineformset_factory

from todo.models import Subject, Assignment
from crispy_forms.helper import FormHelper

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        labels = {
            "name": "Subject Name",
            "cp": "Credit Points",
            "have_exam_permit": "Do you have the Exam Permit?",
            "exam_date": "Exam Date",
            "comment": "Additional Information",
            "team": "Team"
        }
        error_messages = {
            "name": {
                "max_length": "The subject name is too long.",
                "required": "Please enter the subject name.",
            },
            "cp": {
                "required": "Please enter the credit points.",
                "invalid": "Please enter a valid number for credit points.",
            },
            "exam_date": {
                "invalid": "Please enter a valid date for the exam.",
            },
        }
        widgets = {
            "exam_date": forms.DateInput(attrs={"type": "date", "min": datetime.date.today().strftime("%Y-%m-%d")}),
            "comment": forms.Textarea(attrs={"rows": 4}),
            "cp": forms.NumberInput(attrs={"min": 0, "step": 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ("subject",)
        labels = {
            "title": "Assignment Name",
            "description": "Information",
            "deadline": "Deadline"
        }
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local", "min": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

AssignmentFormSet = inlineformset_factory(
    Subject,
    Assignment,
    form=AssignmentForm,
    extra=1,
    can_delete=True
)