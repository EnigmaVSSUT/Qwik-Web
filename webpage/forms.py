from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member, EventRegistration

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 
                'lastname', 
                'email', 
                'year', 
                'profile_pic',
                ]

class MemberRegistrationForm2(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
                'github', 
                'linkedin', 
                'facebook',
                'instagram',
                ]

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = [
            'firstname',
            'lastname',
            'email',
            'year',
            'branch',
            'gender',
        ]
