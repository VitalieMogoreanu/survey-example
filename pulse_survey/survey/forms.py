
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    if not email_address.lower().endswith("@cabinetoffice.gov.uk"):
        raise ValidationError('%(value)s is not a Cabinet Office email', params={'value': email_address})

class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

