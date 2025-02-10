# core/forms.py
from django import forms
from django.utils import timezone
from .models import Contact

class ContactForm(forms.ModelForm):
    contact_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        required=False  # Allow it to be optional
    )

    class Meta:
        model = Contact
        # Fields you want to expose in the form:
        fields = ['subject', 'fname', 'lname', 'email', 'phone', 'message', 'contact_date']
        
    def clean_contact_date(self):
        contact_date = self.cleaned_data.get('contact_date')
        if not contact_date:
            return timezone.now().date()  # Set to today's date if not provided
        return contact_date
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Ensure phone is numeric only
            if not phone.isdigit():
                raise forms.ValidationError("Phone number must be numeric.")
        return phone