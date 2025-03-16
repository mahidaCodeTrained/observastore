from django import forms
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["name", "email", "store_good", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}),
            "store_good": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Your Message"}),
        }
