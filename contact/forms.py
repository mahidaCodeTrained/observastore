from django import forms
from .models import ContactRequest, Newsletter
from storefront.models import StoreGoods


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["name", "email", "store_good", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Email"
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Your Message"
                }
            ),
        }

    store_good = forms.ModelChoiceField(
        queryset=StoreGoods.objects.all(),  # Get all StoreGood objects
        required=True,  # Make sure the field is required
        empty_label="Select a product",  # Placeholder text
        widget=forms.Select(attrs={"class": "form-control"}),
    )


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
