from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from Core.utils.ProjectUtils import CustomRegex

class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        help_text='Enter a valid phone number (e.g., 09123456789 or +989123456789)',
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("phone_number", "email", "first_name", "last_name")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            import re
            if not re.match(CustomRegex.phone_regex, phone_number):
                raise forms.ValidationError("Must be a valid phone number with 10 digits (e.g., 09123456789).")
            
            # Check if phone number already exists
            short_phone = phone_number[-10:]
            if User.objects.filter(phone_number=short_phone).exists():
                raise forms.ValidationError("A user with this phone number already exists.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        phone_number = self.cleaned_data["phone_number"]
        user.phone_number = phone_number[-10:]
        user.username = phone_number[-10:]
        user.slug = phone_number[-10:]
        if commit:
            user.save()
        return user
